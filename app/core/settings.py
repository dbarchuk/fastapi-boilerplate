from functools import lru_cache
from typing import Literal

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application and web server settings
    ENV: Literal["dev", "stage", "production", "test"] = Field(default="dev")
    RELOAD: bool = Field(default=False)
    PORT: int = Field(default=8000)
    WORKERS: int = Field(default=1)
    LOG_LEVEL: Literal["critical", "error", "warning", "info", "debug", "trace"] = Field("info")

    # API INFO settings
    APP_NAME: str = Field("FastAPI")

    # Database settings
    DATABASE_DSN: PostgresDsn = Field('postgres://postgres:postgres@localhost:5432/main-db')

    @property
    def reload(self):
        return self.ENV in ("dev", "test")


@lru_cache
def get_settings():
    return Settings(_env_file="../.env")


settings = get_settings()
