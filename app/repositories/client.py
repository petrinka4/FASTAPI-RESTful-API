from app.repositories.base import BaseRepository
from app.models.client import clientModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

class ClientRepository(BaseRepository):
    Model: DeclarativeMeta = clientModel

    @classmethod
    async def get_accounts(cls, client_id: int, session: AsyncSession):
        client = await super().get_one(client_id, session)
        return client.accounts
