from pydantic import BaseModel


class UploadResponse(BaseModel):
    file_name: str
    original_name: str
    size: int