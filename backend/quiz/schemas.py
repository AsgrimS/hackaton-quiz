from ninja import ModelSchema, Schema
from ninja.orm import create_schema

from quiz.models import Quiz, QuizEntry, Question


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


class QuizInMyListSchema(ModelSchema):
    class Config:
        model = Quiz
        model_fields = ["id", "title", "description", "is_published"]


class UpdateQuizSchema(ModelSchema):
    class Config:
        model = Quiz
        model_fields = ["title", "description", "is_published"]
        model_fields_optional = ["title", "description", "is_published"]


class AnswerSchema(Schema):
    value: list[bool] | str


class LeaderboardEntrySchema(Schema):
    username: str
    score: float
    place: int
    time: float


class QuizCreateInputSchema(Schema):
    title: str
    description: str
    open_questions: int
    closed_questions: int


class QuestionDetailsSchema(ModelSchema):
    class Config:
        model = Question
        model_fields = [
            "question_text",
            "quiz",
            "question_number",
            "question_type",
            "answers",
        ]


class QuizDetailsSchema(ModelSchema):
    questions: list[QuestionDetailsSchema]

    class Config:
        model = Quiz
        model_fields = ["id", "title", "description"]
