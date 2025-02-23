from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


engine = create_async_engine(
    f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session
# async with используется для работы с асинхронными контекстными менеджерами
# это гарантирует, что после завершения работы с session, она будет автоматически закрыта
