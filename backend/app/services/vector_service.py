import chromadb


class VectorService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def store_embeddings(
        self,
        document_id: str,
        file_name: str,
        chunks,
        embeddings,
    ):

        chunk_ids = []

        documents = []

        metadata = []

        for index, chunk in enumerate(chunks):

            chunk_ids.append(
                f"{document_id}_{index}"
            )

            documents.append(
                chunk["text"]
            )

            metadata.append(
                {
                    "document_id": document_id,
                    "file_name": file_name,
                    "page": chunk["page"],
                    "chunk_index": index,
                }
            )

        self.collection.add(
            ids=chunk_ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadata,
        )

    def search(
        self,
        query_embedding,
        top_k: int = 3,
        document_id: str | None = None,
    )-> dict:

        query = {
            "query_embeddings": [query_embedding.tolist()],
            "n_results": top_k,
        }

        if document_id:
            query["where"] = {
                "document_id": document_id
            }

        return self.collection.query(**query)

vector_service = VectorService()