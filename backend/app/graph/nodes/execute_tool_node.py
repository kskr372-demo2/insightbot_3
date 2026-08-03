from app.graph.state import InsightBotState
from app.tools.registry import TOOLS


class ExecuteToolNode:

    def __call__(self, state: InsightBotState):

        tool_name = state["selected_tool"]

        tool_config = TOOLS.get(tool_name)

        if tool_config is None:
            return {
                "answer": "Tool not found."
            }

        tool_function = tool_config["function"]

        accepts_input = tool_config.get(
            "accepts_input",
            False,
        )

        if accepts_input:

            tool_input = state.get(
                "tool_input",
                ""
            )

            result = tool_function(tool_input)

        else:

            result = tool_function()

        return {
            "answer": result
        }