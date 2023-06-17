from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja_extra import Router
from ninja_jwt.authentication import JWTAuth

from quiz.models import Quiz, QuizEntry
from quiz.schemas import QuizEntryInputSchema, QuizEntryOutputSchema, QuizInListSchema

api = Router()


@api.get("/quizzes", response=list[QuizInListSchema])
def list_quizzes(_request: HttpRequest):
    # TODO: filtering, pagination
    return Quiz.objects.filter(is_published=True).order_by("id").all()


@api.post("/quiz-entries", auth=JWTAuth(), response=QuizEntryOutputSchema)
def start_quiz(request, data: QuizEntryInputSchema):
    user: User = request.auth
    quiz: Quiz = get_object_or_404(Quiz, id=data.quiz_id)
    quiz_entry = QuizEntry.create_new(user=user, quiz=quiz)
    return quiz_entry


@api.post("/quiz-entries/{quiz_entry_id}/finish", auth=JWTAuth())
def finish_quiz(request, quiz_entry_id: int):
    user: User = request.auth
    quiz_entry: QuizEntry = get_object_or_404(QuizEntry, id=quiz_entry_id, user=user)

    quiz_entry.finish_quiz()


@api.patch("/quiz-entries/{quiz_entry_id}/answers/{question_no}", auth=JWTAuth())
def add_answer(request, quiz_entry_id: int, question_no: int, answer: str):
    user: User = request.auth
    quiz_entry: QuizEntry = get_object_or_404(QuizEntry, id=quiz_entry_id, user=user)

    quiz_entry.add_answer(question_no=question_no, answer=answer)
