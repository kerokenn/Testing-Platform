from fastapi import APIRouter, Query
from services.exam_delivery_service import ExamDeliveryService

router = APIRouter(prefix="/exams", tags=["Exam Delivery Service"])
service = ExamDeliveryService()


@router.get("/")
async def list_exams(category: str = Query(None), page: int = Query(1)):
    """Return paginated, filterable exam catalog."""
    return await service.list_exams(category=category, page=page)


@router.get("/{exam_id}/start")
async def start_exam(exam_id: str):
    """Fetch and randomize questions for an active exam session."""
    return await service.start_exam(exam_id)
