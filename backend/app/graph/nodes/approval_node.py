from langgraph.types import interrupt

from app.graph.state import InsightBotState
from app.tools.registry import TOOLS


class ApprovalNode:

    def __call__(self, state: InsightBotState):

        tool_name = state["selected_tool"]

        tool = TOOLS.get(tool_name)

        if tool is None:
            return {
                "approved": False
            }

        if tool["requires_approval"]:

            approval =interrupt(
                {
                    "status": "WAITING_FOR_APPROVAL",
                    "tool": tool_name,
                    "message": f"{tool_name} requires approval."
                }
                                )
            return {
                "approved": approval["approved"]
            }

        return {
            "approved": True
        }