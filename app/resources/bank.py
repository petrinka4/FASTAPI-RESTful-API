
from fastapi import HTTPException

from app.models.bank import bankModel
from app.validation.general import ValidateServise
from app.resources.general import GeneralResources

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class BankResources:

    @classmethod
    async def add_bank(cls, data: BaseModel, session: AsyncSession):
        return await GeneralResources.add_one(bankModel, data, session)

    @classmethod
    async def update_bank(cls,  bank_id: int, data, session):
        if (await ValidateServise.validate_id_existence(bankModel, "id", bank_id, session)):
            return await GeneralResources.update_one(bankModel, bank_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
