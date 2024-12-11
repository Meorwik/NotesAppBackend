from .texts_raw import templates_raw, texts_raw
from dataclasses import dataclass
from typing import Final


@dataclass
class Texts:
    ...


@dataclass
class TextTemplates:
    postgres_engine_template: Final[str] = templates_raw["postgres_engine_template"]
    info_logging_template: Final[str] = templates_raw["info_logging_template"]



texts: Final[Texts] = Texts()
texts_templates: Final[TextTemplates] = TextTemplates()

