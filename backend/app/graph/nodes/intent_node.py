from app.graph.state import InsightBotState


class IntentNode:

    def __call__(self, state: InsightBotState):

        question = state["question"].lower()

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
            "thank you",
            "thanks",
            "who are you",
        ]

        if any(word in question for word in greetings):
            return {
                "intent": "general"
            }

        return {
            "intent": "document"
        }