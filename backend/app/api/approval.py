from fastapi import APIRouter

from langgraph.types import Command

from app.graph import graph
from app.schemas.approval import ApprovalRequest

router = APIRouter()


@router.post("/approve")
def approve(request: ApprovalRequest):

    result = graph.invoke(
        Command(
            resume={
                "approved": request.approved
            }
        ),
        config={
            "configurable": {
                "thread_id": request.thread_id
            }
        }
    )

    if request.approved:
        return {
            "success": True,
            "message": "Request approved and tool executed successfully.",
            "data": {
                "thread_id": request.thread_id,
                "status": "COMPLETED",
                "answer": result.get("answer"),
            }
        }

    # Rejected -> graph routed directly to END
    return {
        "success": True,
        "message": "Request rejected.",
        "data": {
            "thread_id": request.thread_id,
            "status": "REJECTED",
        }
    }