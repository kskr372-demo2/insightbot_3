from app.graph.state import InsightBotState


class GeneralAgent:

    def __init__(
        self,
        llm_service,
    ):
        self.llm_service = llm_service

    def run(
        self,
        state: InsightBotState,
    ):

        question = state["question"]

        prompt = f"""
You are InsightBot, an enterprise AI assistant.

Answer the user's general question clearly and professionally.

User Question:
{question}
"""

        answer = self.llm_service.generate_answer(
            prompt
        )

        return {
            "answer": answer
        }