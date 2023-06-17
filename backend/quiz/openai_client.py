import json

import openai
from decimal import Decimal

from django.conf import settings

from core import prompts


class OpenAIClient:
    """OpenAI API client."""

    def __init__(self, api_key: str):
        """Initialize the client."""
        openai.organization = "org-jNm5a0gLyFvSBNatRg6GD8cc"
        openai.api_key = api_key

    def generate_questions_for_quiz(
        self, *, title: str, description: str, open_questions: int, closed_questions: int
    ) -> dict:
        messages = [
            {"role": "system", "content": prompts.QUESTIONS_GENERATING_INTRO},
            {"role": "user", "content": prompts.SAMPLE_QUIZ_REQUEST},
            {"role": "assistant", "content": prompts.SAMPLE_QUIZ_RESPONSE},
            {
                "role": "user",
                "content": prompts.QUIZ_REQUEST.format(
                    title=title,
                    description=description,
                    open_questions=open_questions,
                    closed_questions=closed_questions,
                ),
            },
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        sanitized_content = (
            "{" + response.choices[0].message.content.split("{", 1)[1].rsplit("}", 1)[0] + "}"
        )

        print(f"{sanitized_content=}")
        return json.loads(sanitized_content)

    def check_user_response_against_valid_responses(
        self, question: str, valid_responses: list[str], user_response: str
    ) -> Decimal:
        messages = [
            {"role": "system", "content": prompts.VALIDATE_REQUEST_INTRO},
            {"role": "user", "content": prompts.SAMPLE_VALIDATE_REQUEST},
            {"role": "assistant", "content": prompts.SAMPLE_VALIDATE_RESPONSE},
            {
                "role": "user",
                "content": json.dumps(
                    dict(
                        question=question,
                        user_response=user_response,
                        valid_responses=valid_responses,
                    ),
                ),
            },
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return Decimal(response.choices[0].message.content.strip())


openai_client = OpenAIClient(api_key=settings.OPENAI_API_KEY)
