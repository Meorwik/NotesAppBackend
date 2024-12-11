from logging import StreamHandler, Logger
from typing import Final

DATABASE_LOGS_HANDLER: Final[StreamHandler] = StreamHandler()
DATABASE_LOGGER: Final[Logger] = Logger("Database")
DATABASE_LOGGER.addHandler(DATABASE_LOGS_HANDLER)
