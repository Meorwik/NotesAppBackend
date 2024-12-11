from starlette.responses import JSONResponse
from fastapi import APIRouter, Request
from .auth.auth import auth_router
from .api.api import api_router
from typing import Final
main_router: Final[APIRouter] = APIRouter()
main_router.include_router(auth_router)
main_router.include_router(api_router)

@main_router.get("/")
def index(request: Request):
    return JSONResponse({
        "hello": "world"
    })


