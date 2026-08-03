from app.services.intent_service import intent_service
from app.graph.state import InsightBotState


class IntentNode:

    def __call__(self, state: InsightBotState):

        intent = intent_service.classify(
            state["question"]
        )

        return {
            "intent": intent
        }