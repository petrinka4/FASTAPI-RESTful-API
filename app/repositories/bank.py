
from app.models.account import accountModel
from app.models.branch import branchModel
from app.repositories.base import BaseRepository
from app.models.bank import bankModel

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession


class BankRepository(BaseRepository):
    Model: DeclarativeMeta = bankModel

    @classmethod
    async def get_accounts(
            cls, bank_id: int,
            session: AsyncSession,
            page: int = 1,
            per_page: int = 10
    ):
        try:
            cls.Model = accountModel
            return await super().get_related(
                session=session,
                foreign_key_field=cls.Model.bank_id,
                ID=bank_id,
                page=page,
                per_page=per_page
            )
        finally:
            cls.Model = bankModel  

        

    @classmethod
    async def get_branches(
        cls, bank_id: int,
        session: AsyncSession,
        page: int = 1,
        per_page: int = 10
    ):
        try:
                
            cls.Model = branchModel
            return await super().get_related(
                session=session,
                foreign_key_field=cls.Model.bank_id,
                ID=bank_id,
                page=page,
                per_page=per_page
            )
        finally:
            cls.Model=bankModel
