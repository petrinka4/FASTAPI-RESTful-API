from app.schemas import AccountAddSchema
from app.models.accountModel import accountModel
from app.models.bankModel import bankModel
from app.models.clientModel import clientModel

from app.database import new_session
from sqlalchemy import select, update, insert, delete


class AccountOperations:

    @classmethod
    async def add_one_account(cls, data: AccountAddSchema):
        async with new_session() as session:
            query = select(clientModel).where(clientModel.id == data.client_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"error": "Incorrect client_id"}

            query = select(bankModel).where(bankModel.id == data.bank_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"error": "Incorrect bank_id"}

            if (data.balance < 0):
                return {"ok": False, "error": "Incorrect value of balance"}
            query = (insert(accountModel)
                     .values(bank_id=data.bank_id, client_id=data.client_id, balance=data.balance)
                     .returning(accountModel.id))
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

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
