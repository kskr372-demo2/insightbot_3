from fastapi import APIRouter
router = APIRouter()
from app.schemas.response import ApiResponse
from app.services.search_service import search_service

@router.get(
    "/search",
    response_model=ApiResponse,
)
def search(
    query: str,
):

    result = search_service.ask(query)

    return ApiResponse(
        success=True,
        message="Answer generated successfully.",
        data=result,
    )