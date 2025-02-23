
from app.schemas import BankAddSchema

from app.models.bank import bankModel

from app.database import new_session
from app.operations.general import GeneralOperations

from sqlalchemy import select, text, update, insert
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel


class BankOperations:
    @classmethod
    async def add_bank(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        return await GeneralOperations.add_one(Model, data, session)
        


    @classmethod
    async def update_bank(cls, bank_id, data: BankAddSchema):
        async with new_session() as session:
            query = select(bankModel).where(bankModel.id == bank_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect bank_id"}
            query = update(bankModel).where(
                bankModel.id == bank_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
