from src.database.postgres.postgres import PostgresManager
from src.loggers.fastapi_loggers import FASTAPI_LOGGER
from src.data.config import AppConfig, MetaData
from src.data.texts import texts_templates
from dotenv import load_dotenv
from typing import Final

config: Final[AppConfig] = AppConfig()
meta: Final[MetaData] = MetaData()
postgres: Final[PostgresManager] = PostgresManager(config.POSTGRES_ENGINE)

load_dotenv(dotenv_path='.env')

async def initialize_app() -> None:

    await postgres.init()
    FASTAPI_LOGGER.info(
        msg=texts_templates.info_logging_template.format(
            msg="App was successfully initialized"
        )
    )

