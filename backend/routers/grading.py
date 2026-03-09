from fastapi import APIRouter
from services.grading_service import GradingService

router = APIRouter(prefix="/grading", tags=["Grading Service"])
service = GradingService()


@router.post("/{exam_id}/submit")
async def submit_exam(exam_id: str):
    """Check answers, calculate score, and store result."""
    return await service.submit_exam(exam_id)


@router.get("/{result_id}/review")
async def get_review(result_id: str):
    """Return detailed post-exam review with analytics."""
    return await service.get_review(result_id)
