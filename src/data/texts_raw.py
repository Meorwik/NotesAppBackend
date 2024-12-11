from typing import Final, Dict


postgres_engine_template: Final[str] = "postgresql{driver}://{user}:{password}@{host}:{port}/{database}"
info_logging_template: Final[str] = "INFO:\t  {msg}"



texts_raw: Final[Dict[str, str]] = {

}

templates_raw: Final[Dict[str, str]] = {
    "postgres_engine_template": postgres_engine_template,
    "info_logging_template": info_logging_template
}
