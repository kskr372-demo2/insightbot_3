from app.services.llm_service import llm_service


class IntentService:

    def classify(self, question: str) -> str:

        prompt = f"""You are an intent classifier.

Classify the user's request into exactly one category.

1. document
- Questions that require information from uploaded documents.

2. general
- General conversation, explanations, greetings, knowledge questions, writing assistance.

3. tool
- Requests that require executing a tool or taking an action.

Examples:

User: What is today's date?
tool

User: Generate a random number.
tool

User: Send an email to HR.
tool

User: Create a Jira ticket.
tool

User: Delete customer 123.
tool

Return ONLY:
document
general
tool

User:
{question}
"""

        response = llm_service.generate_answer(prompt)

        intent= response.strip().lower()
        if intent not in {"tool", "general", "document"}:
            intent = "document"
        print("Intent classification result:", intent)
        return intent
    

intent_service = IntentService()