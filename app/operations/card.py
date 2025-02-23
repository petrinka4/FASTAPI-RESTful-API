from fastapi import HTTPException
from app.operations.general import GeneralOperations
from app.schemas import CardAddSchema

from app.models.account import accountModel
from app.models.card import cardModel

from app.database import new_session

from sqlalchemy import select, text, update, insert
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from app.validation.card import validateCard


class CardOperations:

    @classmethod
    async def add_card(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        if (await validateCard(data, session)):
            return await GeneralOperations.add_one(Model, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_card(cls, card_id, data: CardAddSchema):
        async with new_session() as session:
            query = select(cardModel).where(cardModel.id == card_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect card_id"}

            query = select(accountModel).where(
                accountModel.id == data.account_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect account_id"}

            if (data.balance < 0):
                return {"ok": False, "error": "Incorrect value of balance"}
            query = update(cardModel).where(cardModel.id == card_id).values(
                account_id=data.account_id, balance=data.balance)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
