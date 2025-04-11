from app.models.account import accountModel
from app.repositories.base import BaseRepository
from app.models.client import clientModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class ClientRepository(BaseRepository):
    Model: DeclarativeMeta = clientModel

    @classmethod
    async def get_accounts(
            cls, client_id: int,
            session: AsyncSession,
            page: int = 1,
            per_page: int = 10
    ):
        try:
            cls.Model = accountModel
            return await super().get_related(
                session=session,
                foreign_key_field=cls.Model.client_id,
                ID=client_id,
                page=page,
                per_page=per_page
            )
        finally:
            cls.Model = clientModel
