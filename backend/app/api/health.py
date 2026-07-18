from fastapi import APIRouter
from fastapi import Depends
from app.dependencies.settings import get_settings
from app.core.settings import Settings
# from app.core.settings import settings
from app.schemas.response import ApiResponse
router = APIRouter()




@router.get(
    "/health",
    response_model=ApiResponse,
    tags=["Health"]
)
def get_health(settings: Settings = Depends(get_settings),):

    return ApiResponse(
        success=True,
        message="Health check successful",
        data={
            "status": "healthy",
            "service": settings.app_name,
            "version": settings.app_version,
            "environment": settings.app_environment,
        },
    )

