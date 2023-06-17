# Generated by Django 4.2.2 on 2023-06-17 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("question_text", models.TextField()),
                ("question_number", models.IntegerField(default=1)),
                (
                    "question_type",
                    models.CharField(
                        choices=[("open", "Open"), ("closed", "Closed")],
                        default="closed",
                        max_length=6,
                    ),
                ),
                ("answers", models.JSONField(default=dict)),
                (
                    "quiz",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="quiz.quiz"),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="openquestion",
            name="quiz",
        ),
        migrations.DeleteModel(
            name="ClosedQuestion",
        ),
        migrations.DeleteModel(
            name="OpenQuestion",
        ),
    ]