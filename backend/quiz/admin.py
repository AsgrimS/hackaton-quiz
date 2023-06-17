from django.contrib import admin

from quiz.models import OpenQuestion, ClosedQuestion, Quiz

# Register your models here.
admin.site.register([Quiz, OpenQuestion, ClosedQuestion])