from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
        )

    def split_text(
        self,
        pages: list,
    ):
        chunks = []
        for page in pages:
            print(pages)
            page_chunks = self.splitter.split_text(page["text"])
            for chunk in page_chunks:
                chunks.append(
                    {
                        "page": page["page"],
                        "text": chunk,
                    }
                )

        return chunks


chunk_service = ChunkService()