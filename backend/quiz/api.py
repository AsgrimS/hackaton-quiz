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
    AnswerSchema,
    QuizInMyListSchema,
    UpdateQuizSchema,
    QuizCreateInputSchema,
    QuizDetailsSchema,
    QuizMyEntryOutputSchema,
)

quiz_api = Router(auth=JWTAuth())


@quiz_api.get("/quizzes", response=list[QuizInListSchema], auth=None)
def list_quizzes(_request):
    return Quiz.objects.filter(is_published=True).order_by("id").all()


@quiz_api.get("/quizzes/{quiz_id}", response=QuizDetailsSchema)
def single_quiz(_request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return quiz


@quiz_api.get("/my-quizzes", response=list[QuizInMyListSchema])
def my_quizzes(request):
    user: User = request.auth
    return Quiz.objects.filter(author=user).order_by("id").all()


@quiz_api.post("/my-quizzes")
def create_quiz(request, data: QuizCreateInputSchema):
    user: User = request.auth
    quiz = Quiz.create_new(**data.dict(), author=user)
    return quiz.id


@quiz_api.patch("/my-quizzes/{quiz_id}")
def update_quiz(request, quiz_id: int, data: UpdateQuizSchema):
    user: User = request.auth
    quiz = get_object_or_404(Quiz, author=user, id=quiz_id)
    for key, value in data:
        if value is not None:
            setattr(quiz, key, value)
    quiz.save()


@quiz_api.get("/my-quiz-entries", response=QuizMyEntryOutputSchema)
def my_quizzes(request):
    user: User = request.auth
    quiz_entries = QuizEntry.objects.filter(user=user).order_by("id").all()
    return quiz_entries


@quiz_api.post("/quiz-entries", response=QuizEntryOutputSchema)
def start_quiz(request, data: QuizEntryInputSchema):
    user: User = request.auth
    quiz: Quiz = get_object_or_404(Quiz, id=data.quiz, is_published=True)
    quiz_entry = QuizEntry.create_new(user=user, quiz=quiz)
    return quiz_entry


@quiz_api.post("/quiz-entries/{quiz_entry_id}/finish")
def finish_quiz(request, quiz_entry_id: int):
    user: User = request.auth
    quiz_entry: QuizEntry = get_object_or_404(QuizEntry, id=quiz_entry_id, user=user)

    quiz_entry.finish_quiz()


@quiz_api.patch("/quiz-entries/{quiz_entry_id}/answers/{question_no}")
def add_answer(request, quiz_entry_id: int, question_no: int, answer: AnswerSchema):
    user: User = request.auth
    quiz_entry: QuizEntry = get_object_or_404(QuizEntry, id=quiz_entry_id, user=user)

    quiz_entry.add_answer(question_no=question_no, answer=answer.value)


@quiz_api.get("/leaderboard/{quizz_id}", response=list[LeaderboardEntrySchema], auth=None)
def list_leaderboard(_request: HttpRequest, quizz_id):
    # results = (
    #     QuizEntry.objects.filter(finished_at__isnull=False).order_by("score").all()
    # )

    return [
        {"username": "Bob", "score": 100, "place": 1, "time": 126},
        {"username": "John", "score": 90, "place": 2, "time": 306},
        {"username": "Max", "score": 10, "place": 3, "time": 50},
    ]
