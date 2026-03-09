class ExamDeliveryService:
    """
    Queries the DB, handles randomization and pagination for exam delivery.
    Connects to: Firestore — exams, questions collections
    """

    async def list_exams(self, category: str = None, page: int = 1) -> dict:
        # TODO: query Firestore exams collection with filters + pagination
        raise NotImplementedError

    async def start_exam(self, exam_id: str) -> dict:
        # TODO: fetch questions for exam_id, randomize order
        raise NotImplementedError
