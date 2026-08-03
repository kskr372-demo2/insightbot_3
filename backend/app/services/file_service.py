from pathlib import Path

from fastapi import UploadFile
from datetime import datetime
import uuid
from pathlib import Path

from app.repositories.file_repository import file_repository
from app.schemas.file_metadata import FileMetadata
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_service import vector_service
from app.utils.file_utils import (
    UPLOAD_DIR,
    generate_file_name,
    validate_size,
    validate_extension
)
from app.services.pdf_service import pdf_service

class FileService:

    def save_file(
        self,
        file: UploadFile,
    ):
        content = file.file.read()

        validate_size(len(content))
        validate_extension(file.filename)
        new_name = generate_file_name(file.filename)

        destination = UPLOAD_DIR / new_name

        with destination.open("wb") as buffer:
            # buffer.write(file.file.read())
            buffer.write(content)
         # -----------------------------
    # Create metadata
    # -----------------------------    
        metadata = FileMetadata(
            id=str(uuid.uuid4()),
            original_name=file.filename,
            stored_name=new_name,
            extension=Path(file.filename).suffix.lower(),
            size=destination.stat().st_size,
            uploaded_at=datetime.utcnow(),
            status="UPLOADED",
        )

        file_repository.save_metadata(metadata)
        text = pdf_service.extract_text(str(destination))

        from app.services.chunk_service import chunk_service

        chunks = chunk_service.split_text(text)
        from app.services.embedding_service import embedding_service

        embeddings = embedding_service.create_embeddings(chunks)


        

        vector_service.store_embeddings(
        document_id=metadata.id,
        file_name=file.filename,
        chunks=chunks,
        embeddings=embeddings,
                                    )

        # print(f"Total Embeddings: {len(embeddings)}")

        # print(f"Embedding Dimension: {len(embeddings[0])}")

        # print(f"Total Chunks: {len(chunks)}")
        # print("#########################################")
        # print(f"Chunk 1: {chunks[0]}")
        # print("#########################################")
        # print("****************************************")
        # print(chunks[1])  
        # print("****************************************")      
        return {
            "file_name": new_name,
            "original_name": file.filename,
            "size": destination.stat().st_size,
        }


file_service = FileService()

