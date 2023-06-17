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

    def _generate_closed_questions(self, number_of_closed_questions, ):
        for _ in range(number_of_closed_questions):
            ClosedQuestion.objects.create(
                quiz=self,
                question_text=...,
                question_number=...,
                points=...,
                answer_1=...,
                answer_2=...,
                answer_3=...,
                answer_4=...,
                correct_answer_1=...,
                correct_answer_2=...,
                correct_answer_3=...,
                correct_answer_4=...,
            )

    def _generate_open_questions(self, number_of_open_questions):
        for _ in range(number_of_open_questions):
            OpenQuestion.objects.create(
                quiz=self,
                question_text=...,
                question_number=...,
                valid_response=...,
            )


class ClosedQuestion(models.Model):
    question_text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_number = models.IntegerField(default=1)
    points = models.IntegerField(default=0)
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    answer_4 = models.TextField()
    correct_answer_1 = models.BooleanField(default=False)
    correct_answer_2 = models.BooleanField(default=False)
    correct_answer_3 = models.BooleanField(default=False)
    correct_answer_4 = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class OpenQuestion(models.Model):
    question_text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_number = models.IntegerField(default=1)
    valid_response = models.TextField()

    def __str__(self):
        return self.question_text
