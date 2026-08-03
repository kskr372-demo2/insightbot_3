from app.graph.state import InsightBotState


class ToolAgentNode:

    def __init__(self, tool_agent):
        self.tool_agent = tool_agent

    def __call__(self, state: InsightBotState):

        result = self.tool_agent.run(state)

        return result