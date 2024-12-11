from src.routers.endpoints.endpoints import main_router
from loader import initialize_app
from fastapi import FastAPI
from typing import Final

app: Final[FastAPI] = FastAPI()
app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await initialize_app()

