from sqlalchemy import func, select
from app.models.branch import branchModel
from app.repositories.base import BaseRepository
from app.models.city import cityModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class CityRepository(BaseRepository):
    Model: DeclarativeMeta = cityModel

    @classmethod
    async def get_branches(
            cls, city_id: int,
            session: AsyncSession,
            page: int = 1,
            per_page: int = 10
    ):
        try:
            cls.Model = branchModel
            return await super().get_related(
                session=session,
                foreign_key_field=cls.Model.city_id,
                ID=city_id,
                page=page,
                per_page=per_page
            )
        finally:
            cls.Model=cityModel