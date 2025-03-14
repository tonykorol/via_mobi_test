from fastapi import FastAPI

from api.routers.health_check import router as health_router
from api.routers.caption import router as caption_router

app = FastAPI()

app.include_router(health_router)
app.include_router(caption_router)
