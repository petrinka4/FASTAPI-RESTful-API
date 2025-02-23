from fastapi import HTTPException
from app.schemas import AccountAddSchema
from app.operations.general import GeneralOperations

from app.models.account import accountModel
from app.models.bank import bankModel
from app.models.client import clientModel

from app.database import new_session

from sqlalchemy import select, text, update, insert
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from app.validation.account import validateAccount


class AccountOperations:

    @classmethod
    async def add_account(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        if (await validateAccount(data, session)):
            return await GeneralOperations.add_one(Model, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    

    @classmethod
    async def update_account(cls, account_id, data: AccountAddSchema):
        async with new_session() as session:
            query = select(accountModel).where(accountModel.id == account_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect account_id"}
            query = select(bankModel).where(bankModel.id == data.bank_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect bank_id"}
            query = select(clientModel).where(clientModel.id == data.client_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect client_id"}

            if (data.balance < 0):
                return {"ok": False, "error": "Incorrect value of balance"}
            query = update(accountModel).where(accountModel.id == account_id).values(
                bank_id=data.bank_id, client_id=data.client_id, balance=data.balance)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
