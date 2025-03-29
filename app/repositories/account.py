from app.repositories.base import BaseRepository
from app.models.account import accountModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class AccountRepository(BaseRepository):
    Model: DeclarativeMeta = accountModel

    @classmethod
    async def get_cards(cls, account_id: int, session: AsyncSession):
        account = await super().get_one(account_id, session)
        return account.cards

    # @classmethod
    # async def get_bank(cls, account_id: int, session: AsyncSession):
    #     account = await super().get_one(account_id, session)
    #     return account.bank

    # @classmethod
    # async def get_client(cls, account_id: int, session: AsyncSession):
    #     account = await super().get_one(account_id, session)
    #     return account.client
