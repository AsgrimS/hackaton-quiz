from ninja import ModelSchema

from quiz.models import Quiz, QuizEntry


class QuizEntryInputSchema(ModelSchema):
    class Config:
        model = QuizEntry
        model_fields = ["quiz"]


class QuizEntryOutputSchema(ModelSchema):
    class Config:
        model = QuizEntry
        model_fields = ["id"]


class QuizInListSchema(ModelSchema):
    class Config:
        model = Quiz
        model_fields = ["id", "title", "description"]
