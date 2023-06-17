from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def create_new(cls, title, description, number_of_closed_questions, number_of_open_questions):
        quiz = cls(title=title, description=description)
        quiz._generate_open_questions(number_of_open_questions)
        quiz._generate_closed_questions(number_of_closed_questions)
        quiz.save()
        return quiz

    def _generate_closed_questions(
        self,
        number_of_closed_questions,
    ):
        for _ in range(number_of_closed_questions):
            Question.objects.create(
                quiz=self, type="closed", question_text=..., question_number=..., answers={}
            )

    def _generate_open_questions(self, number_of_open_questions):
        for _ in range(number_of_open_questions):
            Question.objects.create(
                quiz=self, type="open", question_text=..., question_number=..., answers={}
            )


class Question(models.Model):
    class QuestionType(models.TextChoices):
        OPEN = "open"
        CLOSED = "closed"

    question_text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_number = models.IntegerField(default=1)
    question_type = models.CharField(max_length=6, default="closed", choices=QuestionType.choices)
    answers = models.JSONField(default=dict)

    def __str__(self):
        return self.question_text
