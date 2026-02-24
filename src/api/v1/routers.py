from fastapi import APIRouter
from .link.routers import router as link_router

router = APIRouter(prefix="/api/v1")

router.include_router(link_router)