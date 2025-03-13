from sqlalchemy.ext.asyncio import async_sessionmaker

from app.config import engine


new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session
# async with используется для работы с асинхронными контекстными менеджерами
# это гарантирует, что после завершения работы с session, она будет автоматически закрыта
