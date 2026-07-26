from app.graph.state import InsightBotState


class RetrieveNode:

    def __init__(
        self,
        embedding_service,
        vector_service,
        citation_service,
    ):
        self.embedding_service = embedding_service
        self.vector_service = vector_service
        self.citation_service = citation_service

    def __call__(self, state: InsightBotState):

        question = state["question"]

        document_id = state.get("document_id")

        # Generate query embedding
        query_embedding = self.embedding_service.create_query_embedding(
            question
        )

        # Search ChromaDB
        results = self.vector_service.search(
            query_embedding=query_embedding,
            document_id=document_id,
        )

        # documents = results["documents"][0]
        documents = results.get("documents", [[]])[0]
        metadata = results.get("metadatas", [[]])[0]

        # metadata = results["metadatas"][0]

        context = "\n\n".join(documents) if documents else ""

        citations = self.citation_service.build_citations(
            metadata
        )

        return {
            "documents": documents,
            "metadata": metadata,
            "context": context,
            "citations": citations,
        }