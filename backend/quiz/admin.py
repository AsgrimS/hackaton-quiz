from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm

from quiz.models import Quiz, Question, QuizEntry


class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 0
    fk_name = "quiz"


# Register your models here.
class QuizCreateForm(ModelForm):
    open_questions = forms.IntegerField(min_value=1, initial=0)
    closed_questions = forms.IntegerField(min_value=1, initial=0)

    class Meta:
        model = Quiz
        fields = ["title", "description", "open_questions", "closed_questions"]
        widgets = {
            "description": AdminTextareaWidget(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        open_questions = cleaned_data.get("open_questions")
        closed_questions = cleaned_data.get("closed_questions")

        if open_questions and closed_questions:
            if open_questions + closed_questions > settings.QUIZ_MAX_QUESTIONS:
                raise forms.ValidationError(
                    f"The sum of open questions and closed questions must be at most {settings.QUIZ_MAX_QUESTIONS}."
                )

        return cleaned_data


class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return QuizCreateForm
        return super().get_form(request, obj, **kwargs)

    def get_inline_instances(self, request, obj=None):
        if obj:
            return super().get_inline_instances(request, obj)
        return []

    def get_inlines(self, request, obj):
        if obj:
            return [QuestionsInline]
        return []

    def save_model(self, request, obj, form, change):
        if not change:
            Quiz.create_new(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                open_questions=form.cleaned_data["open_questions"],
                closed_questions=form.cleaned_data["closed_questions"],
            )
            return
        super().save_model(request, obj, form, change)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizEntry)
