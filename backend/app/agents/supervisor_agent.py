from app.graph.state import InsightBotState
from app.services.llm_service import llm_service


class SupervisorAgent:

    def __init__(self):
        self.llm_service = llm_service

    def route(
        self,
        state: InsightBotState,
    ):

        question = state["question"]

        prompt = f"""
You are the supervisor of an enterprise multi-agent AI system.

Your job is to decide which specialized agent should handle the user's request.

Available agents:

1. rag_agent
- Use for questions that require information from uploaded documents.
- Examples:
  What is my notice period?
  What does the document say about leave policy?
  Summarize the uploaded policy.

2. tool_agent
- Use when the user wants an action performed or needs a system tool.
- Examples:
  Send an email to HR.
  Create a Jira ticket.
  What is today's date?
  Generate a random number.

3. general_agent
- Use for general conversation or general knowledge.
- Examples:
  Hi.
  What is Generative AI?
  Explain machine learning.

4. rag_then_tool
- Use when the request first requires information from an uploaded document
  and then requires an external action using that information.

Examples:
- Find my notice period and email it to HR.
- Find the leave policy and send it by email.
- Get the policy details and create a Jira ticket with them.

Rules:

Return ONLY one of these values:

rag_agent
tool_agent
general_agent
rag_then_tool

Do not provide an explanation.

User Request:
{question}
"""

        response = self.llm_service.generate_answer(
            prompt
        )

        selected_agent = response.strip().lower()

        if selected_agent not in {
            "rag_agent",
            "tool_agent",
            "general_agent",
            "rag_then_tool",
        }:
            return {
                "selected_agent": "general_agent"
            }

        return {
            "selected_agent": selected_agent
        }