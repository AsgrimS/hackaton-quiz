from django.contrib import admin

from quiz.models import Question, Quiz

# Register your models here.
admin.site.register([Quiz, Question])
