from app.schemas.file_metadata import FileMetadata


class FileRepository:

    def save_metadata(
        self,
        metadata: FileMetadata,
    ):

        print("Saving metadata...")

        print(metadata)


file_repository = FileRepository()