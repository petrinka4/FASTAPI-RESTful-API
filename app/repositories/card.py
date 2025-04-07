from pydantic import BaseModel
from app.repositories.base import BaseRepository
from app.models.card import cardModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class CardRepository(BaseRepository):
    Model: DeclarativeMeta = cardModel

    @classmethod
    async def create(cls, schema: BaseModel, session: AsyncSession):
        data = schema.model_dump()
        data.setdefault("balance", 0) 

        obj = cls.Model(**data)
        session.add(obj)
        await session.commit()
        return obj
