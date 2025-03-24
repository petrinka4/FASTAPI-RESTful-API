from app.repositories.base import BaseRepository
from app.models.city import cityModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class CityRepository(BaseRepository):
    Model: DeclarativeMeta = cityModel

    @classmethod
    async def get_branches(cls, city_id: int, session: AsyncSession):
        bank = await super().get_one(city_id, session)
        return bank.branches
