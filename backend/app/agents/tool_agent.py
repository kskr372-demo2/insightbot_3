from app.graph.state import InsightBotState
from app.services.tool_selection_service import tool_selection_service
from app.tools.registry import TOOLS


class ToolAgent:

    def run(
        self,
        state: InsightBotState,
    ):

        question = state["question"]

        # Result passed from another agent, e.g. RAG Agent
        agent_result = state.get(
            "agent_result",
            ""
        )

        # LLM-based tool selection
        selected_tool = tool_selection_service.select(
            question
        )

        if not selected_tool:
            return {
                "selected_tool": None,
                "answer": "No suitable tool was found."
            }

        tool = TOOLS.get(selected_tool)

        if tool is None:
            return {
                "selected_tool": None,
                "answer": "Selected tool is not available."
            }

        return {
            "selected_tool": selected_tool,
            "requires_approval": tool.get(
                "requires_approval",
                False,
            ),
            "tool_input": agent_result,
        }