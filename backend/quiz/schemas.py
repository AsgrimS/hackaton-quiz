from ninja import ModelSchema, Schema

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


class LeaderboardEntrySchema(Schema):
    username: str
    score: float
    place: int
    time: float
