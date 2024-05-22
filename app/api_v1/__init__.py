from fastapi import APIRouter
from .posts.posts import router as post_router

router = APIRouter(prefix="/posts", tags=["Posts"])
router.include_router(router=post_router)
