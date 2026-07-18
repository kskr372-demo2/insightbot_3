from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import (
    EmptyFileException,
    FileTooLargeException,
    UnsupportedFileTypeException,
)

def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "An unexpected error occurred.",
                "data": None,
            },
        )
    
    @app.exception_handler(FileTooLargeException)
    async def file_size_exception_handler(
        request: Request,
        exc: FileTooLargeException,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
                "data": None,
            },
        )
    @app.exception_handler(UnsupportedFileTypeException)
    async def unsupported_file_handler(
        request: Request,
        exc: UnsupportedFileTypeException,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
                "data": None,
            },
        )
    
    @app.exception_handler(EmptyFileException)
    async def empty_file_handler(
        request: Request,
        exc: EmptyFileException,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
                "data": None,
            },
        )