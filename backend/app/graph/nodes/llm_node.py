from app.graph.state import InsightBotState


class LLMNode:

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def __call__(self, state: InsightBotState):

        prompt = state["prompt"]

        answer = self.llm_service.generate_response(prompt)

        return {
            "answer": answer
        }