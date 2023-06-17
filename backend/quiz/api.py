from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja_extra import Router
from ninja_jwt.authentication import JWTAuth

from quiz.models import Quiz, QuizEntry
from quiz.schemas import (
    LeaderboardEntrySchema,
    QuizEntryInputSchema,
    QuizEntryOutputSchema,
    QuizInListSchema,
)

quiz_api = Router()


@quiz_api.get("/quizzes", response=list[QuizInListSchema])
def list_quizzes(_request: HttpRequest):
    return Quiz.objects.filter(is_published=True).order_by("id").all()


@quiz_api.post("/quiz-entries", auth=JWTAuth(), response=QuizEntryOutputSchema)
def start_quiz(request, data: QuizEntryInputSchema):
    user: User = request.auth
    quiz: Quiz = get_object_or_404(Quiz, id=data.quiz, is_published=True)
    quiz_entry = QuizEntry.create_new(user=user, quiz=quiz)
    return quiz_entry


@quiz_api.post("/quiz-entries/{quiz_entry_id}/finish", auth=JWTAuth())
def finish_quiz(request, quiz_entry_id: int):
    user: User = request.auth
    quiz_entry: QuizEntry = get_object_or_404(QuizEntry, id=quiz_entry_id, user=user)

    quiz_entry.finish_quiz()


@quiz_api.patch("/quiz-entries/{quiz_entry_id}/answers/{question_no}", auth=JWTAuth())
def add_answer(request, quiz_entry_id: int, question_no: int, answer: str):
    user: User = request.auth
    quiz_entry: QuizEntry = get_object_or_404(QuizEntry, id=quiz_entry_id, user=user)

    quiz_entry.add_answer(question_no=question_no, answer=answer)


@quiz_api.get("/leaderboard/{quizz_id}", response=list[LeaderboardEntrySchema])
def list_leaderboard(_request: HttpRequest, quizz_id):
    # results = (
    #     QuizEntry.objects.filter(finished_at__isnull=False).order_by("score").all()
    # )

    return [
        {"username": "Bob", "score": 100, "place": 1, "time": 126},
        {"username": "John", "score": 90, "place": 2, "time": 306},
        {"username": "Max", "score": 10, "place": 3, "time": 50},
    ]
