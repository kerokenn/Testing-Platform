from fastapi import APIRouter, Header
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth Service"])
service = AuthService()


@router.post("/verify-token")
async def verify_token(authorization: str = Header(...)):
    """Verify a Firebase ID token and return the user's role."""
    token = authorization.removeprefix("Bearer ")
    return await service.verify_token(token)
