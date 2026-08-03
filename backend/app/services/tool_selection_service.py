from app.services.llm_service import llm_service
from app.tools.registry import TOOLS


class ToolSelectionService:

    def select(self, question: str) -> str | None:

        tool_descriptions = "\n".join(
            f"- {tool_name}: {tool['description']}"
            for tool_name, tool in TOOLS.items()
        )

        prompt = f"""
You are an AI tool selector.

Available tools:

{tool_descriptions}

Rules:
- Return exactly one tool name.
- Do not explain your answer.
- Return only the tool name.

User:
{question}
"""

        response = llm_service.generate_answer(prompt)

        tool = response.strip().lower()

        if tool not in TOOLS:
            return None

        return tool


tool_selection_service = ToolSelectionService()