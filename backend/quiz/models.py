from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


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
