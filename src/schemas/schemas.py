from pydantic import BaseModel
from src.database.postgres.enums import Roles
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    password: str
    role: Roles
    register_date: datetime

