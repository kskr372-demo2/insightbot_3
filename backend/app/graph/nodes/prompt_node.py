from app.graph.state import InsightBotState


class PromptNode:

    def __init__(
        self,
        prompt_builder,
        memory_service
    ):
        self.prompt_builder = prompt_builder
        self.memory_service = memory_service

    def __call__(self, state: InsightBotState):

        question = state["question"]
        documents = state["documents"]

        history = self.memory_service.get_history()

        context = self.prompt_builder.build_context(documents)

        prompt = self.prompt_builder.build_prompt(
            question=question,
            context=context,
            history=history
        )

        return {
            "context": context,
            "prompt": prompt
        }