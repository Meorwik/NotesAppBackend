from fastapi import APIRouter, Request, Response, Depends
from typing import List, Final, Optional, Union

from starlette.responses import JSONResponse

from .dependencies import verify_token


api_router: Final[APIRouter] = APIRouter(
    prefix="/api",
    tags=["api"],
    dependencies=[Depends(verify_token)],
)

@api_router.get("/")
async def root(request: Request):
    return {123: "456"}
