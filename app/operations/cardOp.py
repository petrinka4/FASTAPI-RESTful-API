from app.schemas import CardAddSchema
from app.models.accountModel import accountModel
from app.models.cardModel import cardModel
from app.database import new_session
from sqlalchemy import select, text, update, insert, delete


class CardOperations:

    @classmethod
    async def add_one_card(cls, data: CardAddSchema):
        async with new_session() as session:
            query = select(accountModel).where(
                accountModel.id == data.account_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"error": "Incorrect account_id"}

            if (data.balance < 0):
                return {"ok": False, "error": "Incorrect value of balance"}
            query = (insert(cardModel)
                     .values(account_id=data.account_id, balance=data.balance))
            await session.execute(query)
            await session.commit()
            result = await session.execute(text("SELECT LAST_INSERT_ID()"))

            return result.scalar()

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
