from fastapi import APIRouter

router = APIRouter()


@router.get("/debug-error")
def debug_error():
    raise Exception("This is a test exception.")