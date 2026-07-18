import uuid
from pathlib import Path
from app.exceptions.custom_exceptions import (
    UnsupportedFileTypeException,
    EmptyFileException,
    FileTooLargeException,
)

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(exist_ok=True)


def generate_file_name(original_name: str) -> str:
    extension = Path(original_name).suffix

    return f"{uuid.uuid4()}{extension}"


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".wav",
    ".mp3",
}

MAX_FILE_SIZE = 50 * 1024 * 1024



from pathlib import Path


def validate_extension(filename: str):

    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise UnsupportedFileTypeException(f"Unsupported file type: {extension}"
        )
    
def validate_size(size: int):

    if size == 0:
        raise EmptyFileException("Uploaded file is empty.")

    if size > MAX_FILE_SIZE:
        raise FileTooLargeException("Maximum file size is 50 MB.")