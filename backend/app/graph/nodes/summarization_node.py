from app.graph.state import InsightBotState
from app.services.llm_service import llm_service


class SummarizationNode:

    def __call__(self, state: InsightBotState):

        documents = state.get("documents", [])

        if not documents:
            return {
                "summary": ""
            }

        context = "\n\n".join(documents)

        prompt = f"""
You are an enterprise document summarization assistant.

Summarize the following retrieved document content.

Rules:
- Use only the provided content.
- Do not add outside information.
- Keep the summary concise.
- Preserve important facts, dates, numbers, and policies.

Document Content:

{context}

Summary:
"""

        summary = llm_service.generate_answer(prompt)

        return {
            "summary": summary
        }