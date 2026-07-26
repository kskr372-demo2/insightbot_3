from app.graph import graph
from app.services.memory_service import memory_service


class SearchService:

    def ask(
        self,
        question: str,
        document_id: str| None = None,
    ):

        result = graph.invoke(
            {
                "question": question,
                "document_id": document_id,
            }
        )

        memory_service.add_message(
            "user",
            question,
        )

        memory_service.add_message(
            "assistant",
            result["answer"],
        )

        return {
            "question": question,
            "answer": result["answer"],
            "citations": result.get("citations", []),
            "context": result.get("documents", []),
        }
    


search_service = SearchService()