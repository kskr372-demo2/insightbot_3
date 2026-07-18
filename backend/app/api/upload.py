from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from app.schemas.response import ApiResponse
from app.services.file_service import file_service

router = APIRouter()


@router.post(
    "/upload",
    response_model=ApiResponse,
    tags=["Upload"],
)
def upload_file(
    file: UploadFile = File(...),
):

    result = file_service.save_file(file)

    return ApiResponse(
        success=True,
        message="File uploaded successfully.",
        data=result,
    )