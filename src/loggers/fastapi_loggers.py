from logging import StreamHandler, Logger, INFO
from typing import Final

FASTAPI_LOGS_HANDLER: Final[StreamHandler] = StreamHandler()
FASTAPI_LOGGER: Final[Logger] = Logger("App")
FASTAPI_LOGGER.addHandler(FASTAPI_LOGS_HANDLER)
FASTAPI_LOGGER.setLevel(INFO)