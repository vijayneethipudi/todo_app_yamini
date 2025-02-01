from fastapi import APIRouter

from packages.endpoints import todo_endpoints

router = APIRouter()
router.include_router(todo_endpoints.router)
