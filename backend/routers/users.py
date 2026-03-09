from fastapi import APIRouter
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["User Service"])
service = UserService()


@router.get("/{user_id}")
async def get_user_profile(user_id: str):
    """Retrieve a user's profile and permissions."""
    return await service.get_profile(user_id)


@router.put("/{user_id}")
async def update_user_profile(user_id: str):
    """Update a user's profile."""
    return await service.update_profile(user_id)
