from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2",local_files_only=True)#,local_files_only=True

    # def create_embeddings(self,chunks: list[str],):
    #     return self.model.encode(chunks)
    def create_embeddings(
            self,
            chunks: list,
        ):

            texts = []

            for chunk in chunks:
                texts.append(
                    chunk["text"]
                )

            return self.model.encode(texts)
    def create_query_embedding(self,query: str,):
        return self.model.encode(query)


embedding_service = EmbeddingService()