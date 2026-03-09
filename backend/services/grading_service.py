class GradingService:
    """
    Checks answers, calculates scores, and generates analytics.
    Connects to: Firestore — questions, results collections
    """

    async def submit_exam(self, exam_id: str) -> dict:
        # TODO: compare submitted answers against correct answers, compute score, save to results
        raise NotImplementedError

    async def get_review(self, result_id: str) -> dict:
        # TODO: fetch result + full question details for post-exam review
        raise NotImplementedError
