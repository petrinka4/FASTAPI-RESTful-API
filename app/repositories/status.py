from app.repositories.base import BaseRepository
from app.models.social_status import social_statusModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class StatusRepository(BaseRepository):
    Model: DeclarativeMeta = social_statusModel

    @classmethod
    async def get_clients(cls, status_id: int, session: AsyncSession):
        status = await super().get_one(status_id, session)
        return status.clients
