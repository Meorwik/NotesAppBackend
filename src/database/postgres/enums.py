from typing import Final
from enum import Enum


class Roles(Enum):
    user: Final[str] = "user"
    reviewer: Final[str] = "reviewer"
    admin: Final[str] = "admin"

