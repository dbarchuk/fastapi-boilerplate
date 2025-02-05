from functools import cached_property, lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application and web server settings
    ENV: Literal["dev", "stage", "production", "test"] = Field(default="dev")
    RELOAD: bool = Field(default=False)
    PORT: int = Field(default=8000)
    WORKERS: int = Field(default=1)

    # LOGS
    LOG_LEVEL: Literal["critical", "error", "warning", "info", "debug", "trace"] = Field("info")
    LOGFIRE_TOKEN: str | None = Field(None)

    # API INFO settings
    APP_NAME: str = Field("FastAPI")

    # Database settings
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_USER: str = Field(...)
    POSTGRES_DB: str = Field(...)
    POSTGRES_HOST: str = Field("localhost")
    POSTGRES_PORT: int = Field(5432)
    POSTGRES_ECHO: bool = Field(False)

    @cached_property
    def reload(self):
        return self.ENV in ("dev", "test")

    @cached_property
    def postgres_uri(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"

    @cached_property
    def postgres_uri_sync(self) -> str:
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"


@lru_cache
def get_settings():
    from dotenv import load_dotenv
    load_dotenv()
    return Settings()


settings = get_settings()
