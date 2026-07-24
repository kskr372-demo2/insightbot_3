from app.graph.state import InsightBotState


class RetrieveNode:

    def __init__(
        self,
        embedding_service,
        vector_service,
        citation_service
    ):
        self.embedding_service = embedding_service
        self.vector_service = vector_service
        self.citation_service = citation_service

    def __call__(self, state: InsightBotState):

        question = state["question"]

        # Generate embedding
        query_embedding = self.embedding_service.generate_embedding(question)

        # Search vector DB
        documents = self.vector_service.search(query_embedding)

        # Generate citations
        citations = self.citation_service.generate(documents)

        return {
            "documents": documents,
            "citations": citations
        }