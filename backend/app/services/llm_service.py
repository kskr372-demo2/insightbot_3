from google import genai

from app.core.settings import settings

from app.services.prompt_builder import prompt_builder
class LLMService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate_answer(
        self,
        question: str,
        context: str,
        conversation_history: list,
    ):

        prompt = prompt_builder.build_rag_prompt(
            question=question,
            context=context,
            conversation_history=conversation_history,
        )

        response = self.client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
        )
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(prompt)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        
        return response.text
    

    


llm_service = LLMService()