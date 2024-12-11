from fastapi import Request, APIRouter
from typing import Final

from starlette.responses import JSONResponse

auth_router: Final[APIRouter] = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.get("/login")
async def auth(request: Request):
    return JSONResponse({
        "hello": "world"
    })
