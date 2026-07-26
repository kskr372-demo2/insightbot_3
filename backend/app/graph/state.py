from typing import Any, Dict, List
from typing_extensions import TypedDict


class InsightBotState(TypedDict, total=False):

    question: str

    document_id: str

    documents: List[str]

    metadata: List[Dict[str, Any]]

    citations: List[Dict[str, Any]]

    context: str

    prompt: str

    answer: str

    intent: str

    summary: str

    translated_answer: str
    intent: str