from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.debug import router as debug_router
from app.core.settings import settings
from app.api.upload import router as upload_router
from app.api.search import router as search_router
api_router = APIRouter(prefix=settings.api_prefix)

api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    debug_router,
    tags=["Debug"],
)

api_router.include_router(
    upload_router,
    tags=["Upload"],
)

api_router.include_router(
    search_router,
    tags=["Search"],
)