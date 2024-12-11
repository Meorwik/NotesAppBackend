from enum import Enum
from typing import List, Dict

class LanguageData(Enum):

    ...

    def get_texts(self) -> Dict[str, str]:
        ...