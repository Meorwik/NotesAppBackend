from fastapi import HTTPException, Header
from typing import Final

API_KEY: Final[str] = "12345qwerty"


async def verify_token(authorization: str = Header(...)):
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail='Unauthorized')