

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
    def DATABASE_URL(self) -> MySQLDsn:
        return MySQLDsn.build(
            scheme=str(self.scheme),
            username=str(self.user),
            password=str(self.password),
            host=str(self.host),
            port=self.port,
            path=str(self.path)
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env-template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    db: DatabaseConfig

    


settings = Settings()

