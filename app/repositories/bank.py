from app.repositories.base import BaseRepository
from app.models.bank import bankModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class BankRepository(BaseRepository):
    Model: DeclarativeMeta = bankModel

    @classmethod
    async def get_accounts(cls, bank_id: int, session: AsyncSession):
        bank = await super().get_one(bank_id, session)
        return bank.accounts
    @classmethod
    async def get_branches(cls, bank_id: int, session: AsyncSession):
        bank = await super().get_one(bank_id, session)
        return bank.branches

