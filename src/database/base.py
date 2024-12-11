from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from src.loggers.database_loggers import DATABASE_LOGGER
from src.data.texts import texts_templates


Base = declarative_base()


class DatabaseManager:
    __name__ = "DatabaseManager"

    def __init__(self, engine):
        self.engine: AsyncEngine = create_async_engine(engine)
        self.Session = async_sessionmaker(bind=self.engine)

        DATABASE_LOGGER.info(
            msg=texts_templates.info_logging_template.format(
                msg=f"{self.__name__} was successfully created"
            )
        )