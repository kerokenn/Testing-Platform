class UserService:
    """
    Manages user profiles and permissions.
    Connects to: Firestore — users collection
    """

    async def get_profile(self, user_id: str) -> dict:
        # TODO: fetch from Firestore users/{user_id}
        raise NotImplementedError

    async def update_profile(self, user_id: str) -> dict:
        # TODO: update Firestore users/{user_id}
        raise NotImplementedError
