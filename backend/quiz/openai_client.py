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
    ) -> list:
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

        return json.loads(response.choices[0].message.content)

    def check_user_response_against_valid_responses(
        self, question: str, valid_responses: list[str], user_response: str
    ) -> Decimal:
        def _build_prompt(self, question: str, valid_responses: list[str], user_response: str):
            return f"""
                Question: {question}
                Valid responses: {valid_responses}
                User response: {user_response}
                Score:"""

        """Check if question is valid against valid_responses."""
        prompt = _build_prompt(question, valid_responses, user_response)
        response = openai.ChatCompletion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.3,
            max_tokens=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"],
        )
        return Decimal(response.choices[0].text)


openai_client = OpenAIClient(api_key=settings.OPENAI_API_KEY)
