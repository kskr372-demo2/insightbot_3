from typing import Any, Dict, List, Optional
from typing_extensions import TypedDict


class InsightBotState(TypedDict, total=False):
    # User Input
    question: str

    # Retrieval
    documents: List[Any]
    citations: List[Dict[str, Any]]

    # Prompt
    context: str
    prompt: str

    # LLM Output
    answer: str

    # Future Fields
    intent: str
    summary: str
    translated_answer: str