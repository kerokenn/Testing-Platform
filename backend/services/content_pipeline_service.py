class ContentPipelineService:
    """
    Handles CSV/OCR uploads, parsing, and data tagging for the question bank.
    Connects to: Firestore — questions collection
    """

    async def process_csv(self, file) -> dict:
        # TODO: parse CSV rows into Question documents, write to Firestore
        raise NotImplementedError

    async def process_ocr(self, file) -> dict:
        # TODO: run OCR on image/PDF, extract text, parse into Question documents
        raise NotImplementedError
