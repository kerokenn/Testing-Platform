from fastapi import APIRouter, UploadFile, File
from services.content_pipeline_service import ContentPipelineService

router = APIRouter(prefix="/content", tags=["Content Pipeline Service"])
service = ContentPipelineService()


@router.post("/upload/csv")
async def upload_csv(file: UploadFile = File(...)):
    """Ingest questions from a CSV file."""
    return await service.process_csv(file)


@router.post("/upload/ocr")
async def upload_ocr(file: UploadFile = File(...)):
    """Extract questions from an image/PDF via OCR."""
    return await service.process_ocr(file)
