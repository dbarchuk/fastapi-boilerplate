from fastapi import APIRouter

from .users_router import router as users_router

v1router = APIRouter(tags=["v1"], prefix="/v1")
v1router.include_router(users_router)
