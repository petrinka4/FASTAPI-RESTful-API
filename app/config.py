from sqlalchemy.ext.asyncio import create_async_engine

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DatabaseConfig(BaseModel):
    user: str
    password: str
    host: str
    port: str
    name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env-template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    db: DatabaseConfig


settings = Settings()

DB_USER = settings.db.user
DB_PASSWORD = settings.db.password
DB_HOST = settings.db.host
DB_PORT = settings.db.port
DB_NAME = settings.db.name


engine = create_async_engine(
    f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
