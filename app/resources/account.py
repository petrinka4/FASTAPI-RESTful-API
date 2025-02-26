from fastapi import HTTPException

from app.resources.general import GeneralResources
from app.models.account import accountModel
from app.validation.account import validateAccount
from app.validation.general import ValidateServise

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

# эти и все последующие функции resources вызываются
# в routers внутри блока try.
# здесь есть только add и update потому что для каждой таблицы присутствуют
# индивидуальные проверки для этих двух ресурсов (validation внутри if см. ниже),
# после эттих проверок вызывается общая для всех таблиц функция add или update
# находящаяся в general в этой же директории
# следовательно оставшиеся ресурсы находятся там же


class AccountResources:

    @classmethod
    async def add_account(cls, data: BaseModel, session: AsyncSession):
        if (await validateAccount(data, session)):
            return await GeneralResources.add_one(accountModel, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_account(cls,  account_id: int, data, session):
        if (await validateAccount(data, session) and await ValidateServise.validate_id_existence(accountModel, "id", account_id, session)):
            return await GeneralResources.update_one(accountModel, account_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
