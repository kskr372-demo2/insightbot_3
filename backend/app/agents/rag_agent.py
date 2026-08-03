from app.graph.state import InsightBotState


class RAGAgent:

    def __init__(
        self,
        retrieve_node,
        summarization_node,
        security_node,
        prompt_node,
        llm_node,
    ):
        self.retrieve_node = retrieve_node
        self.summarization_node = summarization_node
        self.security_node = security_node
        self.prompt_node = prompt_node
        self.llm_node = llm_node

    def run(self, state: InsightBotState):

        # Step 1: Retrieve documents
        retrieve_result = self.retrieve_node(state)

        working_state = {
            **state,
            **retrieve_result,
        }

        # Step 2: Summarization
        summary_result = self.summarization_node(
            working_state
        )

        # Step 3: Security validation
        security_result = self.security_node(
            working_state
        )

        working_state = {
            **working_state,
            **summary_result,
            **security_result,
        }

        # Step 4: Build prompt
        prompt_result = self.prompt_node(
            working_state
        )

        working_state = {
            **working_state,
            **prompt_result,
        }

        # Step 5: Generate answer
        answer_result = self.llm_node(
            working_state
        )

        return {
            **working_state,
            **answer_result,
        }