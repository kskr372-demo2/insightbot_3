from app.graph.state import InsightBotState
from app.services.tool_selection_service import tool_selection_service


class ToolNode:

    def __call__(self, state: InsightBotState):

        question = state["question"]

        selected_tool = tool_selection_service.select(question)

        return {
            "selected_tool": selected_tool
        }