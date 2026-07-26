from google import genai

from app.core.settings import settings


class LLMService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate_answer(self, prompt: str) -> str:
        """
        Sends the prepared prompt to Gemini and returns the generated answer.
        """

        response = self.client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
        )

        return response.text


llm_service = LLMService()