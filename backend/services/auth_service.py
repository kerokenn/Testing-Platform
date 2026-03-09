class AuthService:
    """
    Handles Firebase ID token verification and role validation.
    Connects to: Firebase Auth (via firebase-admin SDK)
    """

    async def verify_token(self, token: str) -> dict:
        # TODO: firebase_admin.auth.verify_id_token(token)
        raise NotImplementedError
