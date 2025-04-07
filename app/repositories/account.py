from sqlalchemy import func, select
from app.models.card import cardModel
from app.repositories.base import BaseRepository
from app.models.account import accountModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class AccountRepository(BaseRepository):
    Model: DeclarativeMeta = accountModel

    @classmethod
    async def get_cards(
            cls, account_id: int,
            session: AsyncSession,
            page: int = 1,
            per_page: int = 10
    ):
        try:
            cls.Model = cardModel
            return await super().get_related(
                session=session,
                foreign_key_field=cls.Model.account_id,
                ID=account_id,
                page=page,
                per_page=per_page
            )
        finally:
            cls.Model=accountModel

