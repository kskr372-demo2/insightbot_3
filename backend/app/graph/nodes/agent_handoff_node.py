from app.graph.state import InsightBotState


class AgentHandoffNode:

    def __call__(self, state: InsightBotState):

        answer = state.get("answer", "")

        return {
            "agent_result": answer
        }