import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    POSTGRES_DB: str | None = None
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding='utf-8',
        extra='ignore'  # Игнорировать лишние переменные без ошибок
    )


settings = Settings()


def get_db_url():
    if settings.POSTGRES_USER and settings.POSTGRES_PASSWORD:
        # Используем параметры из docker-compose
        return (
            f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.POSTGRES_DB or settings.DB_NAME}"
        )
        # Используем стандартные параметры
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )
