from app.schemas import BankAddSchema
from app.models.bankModel import bankModel
from app.database import new_session
from sqlalchemy import select, update, insert, delete


class BankOperations:

    @classmethod
    async def add_one_bank(cls, data: BankAddSchema):
        async with new_session() as session:
            query = (insert(bankModel)
                     .values(name=data.name)
                     .returning(bankModel.id))
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

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
