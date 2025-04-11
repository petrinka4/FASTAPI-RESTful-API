from pydantic import MySQLDsn
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.config import settings

from sqlalchemy.ext.asyncio import create_async_engine



DB_URL: MySQLDsn = settings.MYSQL.DATABASE_URL()

engine = create_async_engine(str(DB_URL))

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

