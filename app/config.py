from sqlalchemy.ext.asyncio import create_async_engine

from pydantic import BaseModel, MySQLDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DatabaseConfig(BaseModel):
    scheme: str
    user: str
    password: str
    host: str
    port: int
    path: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env-template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    db: DatabaseConfig

    def DATABASE_URL(self) -> MySQLDsn:
        return MySQLDsn.build(
            scheme=str(self.db.scheme),
            username=str(self.db.user),
            password=str(self.db.password),
            host=str(self.db.host),
            port=self.db.port,
            path=str(self.db.path)
        )


settings = Settings()
DB_URL: MySQLDsn = settings.DATABASE_URL()

engine = create_async_engine(str(DB_URL))
