from app.graph.state import InsightBotState


class GeneralAgentNode:

    def __init__(self, general_agent):
        self.general_agent = general_agent

    def __call__(self, state: InsightBotState):

        result = self.general_agent.run(state)

        return result