from app.graph import graph
from app.services.memory_service import memory_service
import uuid

class SearchService:

    def ask(
        self,
        question: str,
        document_id: str| None = None,
        thread_id: str | None = None,
    ):
        if thread_id is None:
            thread_id = str(uuid.uuid4())

        result = graph.invoke(
            {
                "question": question,
                "document_id": document_id,
            },
            config={
        "configurable": {
            "thread_id": thread_id}
                    }
                                )

        if "__interrupt__" in result:
            interrupt = result["__interrupt__"][0]
            return {
            "thread_id": thread_id,
            "status": interrupt.value["status"],
            "tool": interrupt.value["tool"],
            "message": interrupt.value["message"],
                    }
        memory_service.add_message(
            "user",
            question,
        )
        memory_service.add_message(
            "assistant",
            result["answer"],
        )

        return {
            "thread_id": thread_id,
            "question": question,
            "answer": result["answer"],
            "citations": result.get("citations", []),
            "context": result.get("documents", []),
        }
    


search_service = SearchService()