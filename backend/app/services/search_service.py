from app.services.citation_service import citation_service
from app.services.memory_service import memory_service
from app.services.embedding_service import embedding_service
from app.services.llm_service import llm_service
from app.services.vector_service import vector_service


class SearchService:

    def ask(
        self,
        question: str,
    ):

        history = memory_service.get_history()
        embedding = embedding_service.create_query_embedding(
            question
        )

        results = vector_service.search(
            embedding,document_id=document_id,
        )

        documents = results["documents"][0]
        metadata = results["metadatas"][0]
        citations = citation_service.build_citations(metadata)

        context = "\n\n".join(documents)
        
        answer = llm_service.generate_answer(
            question=question,
            context=context,
            conversation_history=history,
        )
        memory_service.add_message(
            "user",
            question,
        )

        memory_service.add_message(
            "assistant",
            answer,
        )

        return {
            "question": question,
            "answer": answer,
            "citations": citations,
            "context": documents,
        }


search_service = SearchService()