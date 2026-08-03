from app.graph.state import InsightBotState


class SupervisorNode:

    def __init__(self, supervisor_agent):
        self.supervisor_agent = supervisor_agent

    def __call__(self, state: InsightBotState):

        result = self.supervisor_agent.route(state)

        return result