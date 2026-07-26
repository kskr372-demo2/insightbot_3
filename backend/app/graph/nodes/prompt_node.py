from app.graph.state import InsightBotState


class PromptNode:

    def __init__(
        self,
        prompt_builder,
        memory_service,
    ):
        self.prompt_builder = prompt_builder
        self.memory_service = memory_service

    def __call__(self, state: InsightBotState):

        history = self.memory_service.get_history()

        prompt = self.prompt_builder.build_rag_prompt(
            question=state["question"],
            context=state["context"],
            conversation_history=history,
        )

        return {
            "prompt": prompt
        }