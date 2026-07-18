from datetime import datetime

from pydantic import BaseModel


class FileMetadata(BaseModel):
    id: str
    original_name: str
    stored_name: str
    extension: str
    size: int
    uploaded_at: datetime
    status: str