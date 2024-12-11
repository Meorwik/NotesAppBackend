from typing import Final
from .english import EnglishData
from .kazakh import KazakhData
from .russian import RussianData


class LanguagePack:

    english: Final[EnglishData] = EnglishData()
    russian: Final[RussianData] = RussianData()
    kazakh: Final[KazakhData] = KazakhData()