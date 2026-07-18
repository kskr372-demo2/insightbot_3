import logging

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.logging import configure_logging
from app.core.settings import settings
from app.exceptions.handlers import register_exception_handlers
from app.middleware.request_logger import request_logging_middleware
configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise Multimodal Intelligence Platform",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.middleware("http")(request_logging_middleware)
# app.include_router(health_router)
from app.api.router import api_router

app.include_router(api_router)

register_exception_handlers(app)
@app.on_event("startup")
async def startup_event():
    logger.info("Application started successfullyyyy.")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application stopped.")


@app.get("/", tags=["Root"])
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "environment": settings.app_environment,
    }