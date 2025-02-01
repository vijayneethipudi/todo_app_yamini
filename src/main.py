import uvicorn
from fastapi import FastAPI

from packages.routes.api import router as api_router

app = FastAPI()

app.include_router(api_router)
