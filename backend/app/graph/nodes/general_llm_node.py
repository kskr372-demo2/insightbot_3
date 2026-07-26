from app.graph.state import InsightBotState


class GeneralLLMNode:

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def __call__(self, state: InsightBotState):

        prompt = f"""
You are a helpful AI assistant.

Answer the user's question naturally.

Question:
{state["question"]}
"""

        answer = self.llm_service.generate_answer(prompt)

        return {
            "answer": answer
        }