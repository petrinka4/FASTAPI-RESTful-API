from app.models.client import clientModel
from app.repositories.base import BaseRepository
from app.models.social_status import social_statusModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class StatusRepository(BaseRepository):
    Model: DeclarativeMeta = social_statusModel

    @classmethod
    async def get_clients(
            cls, status_id: int,
            session: AsyncSession,
            page: int = 1,
            per_page: int = 10
    ):
        try:

            cls.Model = clientModel
            return await super().get_related(
                session=session,
                foreign_key_field=cls.Model.status_id,
                ID=status_id,
                page=page,
                per_page=per_page
            )
        finally:
            cls.Model = social_statusModel
