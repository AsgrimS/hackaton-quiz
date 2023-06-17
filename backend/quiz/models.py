from django.db import models, transaction
from django.utils import timezone

from quiz.openai_client import openai_client


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def create_new(cls, *, title, description, open_questions, closed_questions):
        quiz = cls(title=title, description=description)
        quiz.save()

        quiz._generate_questions(open_questions, closed_questions)

        return quiz

    def _generate_questions(self, open_questions, closed_questions):
        result = openai_client.generate_questions_for_quiz(
            title=self.title,
            description=self.description,
            open_questions=open_questions,
            closed_questions=closed_questions,
        )

        for num, question in enumerate(result["questions"], 1):
            Question.objects.create(
                quiz=self,
                question_type=question["type"],
                question_text=question["question"],
                question_number=num,
                answers=question["answers"],
            )


class Question(models.Model):
    class QuestionType(models.TextChoices):
        OPEN = "open"
        CLOSED = "closed"

    question_text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_number = models.IntegerField(default=1)
    question_type = models.CharField(
        max_length=6, default="closed", choices=QuestionType.choices
    )
    answers = models.JSONField(default=dict)

    def __str__(self):
        return self.question_text


class AppError(Exception):
    pass


class QuizEntry(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    answers = models.JSONField(default=dict)
    score = models.FloatField(null=True)

    @classmethod
    def create_new(cls, user, quiz):
        quiz_entry = cls(user=user, quiz=quiz)
        quiz_entry.save()
        return quiz_entry

    def add_answer(self, question_no, answer):
        self._validate_answer_does_not_exist_yet(question_no)
        self.answers[question_no] = {
            "answer": answer,
            "score": self._calculate_score(question_no, answer),
        }
        self.save()

    def finish_quiz(self):
        self.finished_at = timezone.now()

    def _validate_answer_does_not_exist_yet(self, question_no):
        if question_no in self.answers:
            raise AppError("Answer already exists")

    def _calculate_score(self, question_no, answer):
        question = self.quiz.question_set.get(question_number=question_no)
        if question.question_type == "closed":
            self._validate_closed_answer(answer, question)
            return self._calculate_closed_question_score(question, answer)
        else:
            return self._calculate_open_question_score(question, answer)

    def _calculate_closed_question_score(self, question: Question, answer: list[bool]):
        correct_answers = question.answers.correct
        return sum(1 for a, b in zip(answer, correct_answers) if a == b) / len(
            correct_answers
        )

    def _validate_closed_answer(self, answer, question):
        if type(answer) != list:
            raise AppError("Answer is not valid")
        if len(answer) != len(question.answers.correct):
            raise AppError("Answer is not valid")

    def _calculate_open_question_score(self, question, answer):
        # check validity of the answer using openai chatgpt api
        return 0.5
