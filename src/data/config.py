from dataclasses import dataclass, field
from .texts import texts_templates
from typing import Final
from os import environ


@dataclass
class PostgresConnectionConfig:
    POSTGRES_DRIVER: Final[str] = "+asyncpg"
    POSTGRES_HOST: Final[str] = 'localhost'
    POSTGRES_PORT: Final[str] = '5432'
    POSTGRES_USER: Final[str] = 'postgres'
    POSTGRES_PASSWORD: Final[str] = '123'
    POSTGRES_DATABASE: Final[str] = 'Notes'


@dataclass
class RedisConnectionConfig:
    HOST: Final[str] = environ.get("REDIS_HOST")
    PORT: Final[int] = 123 #int(environ.get("REDIS_PORT"))
    PASSWORD: Final[str] = environ.get("REDIS_PASSWORD")



@dataclass
class AppConfig:
    POSTGRES_CONFIG: Final[PostgresConnectionConfig] = field(default_factory=PostgresConnectionConfig)
    REDIS_CONFIG: Final[RedisConnectionConfig] = field(default_factory=RedisConnectionConfig)

    _postgres_engine: str = None

    @property
    def POSTGRES_ENGINE(self) -> str:
        if self._postgres_engine is None:

            engine: str = texts_templates.postgres_engine_template.format(
                driver=self.POSTGRES_CONFIG.POSTGRES_DRIVER,
                host=self.POSTGRES_CONFIG.POSTGRES_HOST,
                port=self.POSTGRES_CONFIG.POSTGRES_PORT,
                user=self.POSTGRES_CONFIG.POSTGRES_USER,
                password=self.POSTGRES_CONFIG.POSTGRES_PASSWORD,
                database=self.POSTGRES_CONFIG.POSTGRES_DATABASE,
            )

            self._postgres_engine = engine

        return self._postgres_engine

@dataclass
class MetaData:
    ...


