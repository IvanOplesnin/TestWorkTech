from fastapi import APIRouter, Depends

from backend.schemas import ResponseUser
from backend.security.dependencies import get_current_user

user_router = APIRouter(prefix="/user")


@user_router.get("/", response_model=ResponseUser)
async def get_user(user=Depends(get_current_user)):
    return user
