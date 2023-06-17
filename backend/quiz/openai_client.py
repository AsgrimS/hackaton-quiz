import openai
from decimal import Decimal


class OpenAIClient:
    """OpenAI API client."""

    def __init__(self, api_key: str):
        """Initialize the client."""
        openai.organization = "org-9QX0Z0QXQX0QX0QX"
        openai.api_key = api_key

    def check_user_response_against_valid_responses(
        self, question: str, valid_responses: list[str], user_response: str
    ) -> Decimal:
        """Check if question is valid against valid_responses."""
        prompt = self._build_prompt(question, valid_responses, user_response)
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

    def _build_prompt(self, question: str, valid_responses: list[str], user_response: str):
        return f"""
            Question: {question}
            Valid responses: {valid_responses}
            User response: {user_response}
            Score:"""
