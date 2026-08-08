# from sentence_transformers import SentenceTransformer

# class EmbeddingService:

#     def __init__(self):
#         self.model = SentenceTransformer("all-MiniLM-L6-v2",local_files_only=True)#,local_files_only=True

#     def create_embeddings(
#             self,
#             chunks: list,
#         ):

#             texts = []

#             for chunk in chunks:
#                 texts.append(
#                     chunk["text"]
#                 )

#             return self.model.encode(texts)
#     def create_query_embedding(self,query: str,):
#         return self.model.encode(query)


# embedding_service = EmbeddingService()

from google import genai
from app.core.settings import settings


class EmbeddingService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = "gemini-embedding-001"

    def create_embeddings(self, chunks: list):
        texts = []

        for chunk in chunks:
            texts.append(chunk["text"])

        result = self.client.models.embed_content(
            model=self.model,
            contents=texts,
        )

        return [embedding.values for embedding in result.embeddings]

    def create_query_embedding(self, query: str):
        result = self.client.models.embed_content(
            model=self.model,
            contents=query,
        )

        return result.embeddings[0].values


embedding_service = EmbeddingService()