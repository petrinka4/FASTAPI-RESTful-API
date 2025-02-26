from fastapi import HTTPException

from app.resources.general import GeneralResources
from app.validation.client import validateClient
from app.validation.general import ValidateServise
from app.models.client import clientModel

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class ClientResources:

    @classmethod
    async def add_client(cls, data: BaseModel, session: AsyncSession):
        if (await validateClient(data, session)):
            return await GeneralResources.add_one(clientModel, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_client(cls,  client_id: int, data, session):
        if (await validateClient(data, session) and await ValidateServise.validate_id_existence(clientModel, "id", client_id, session)):
            return await GeneralResources.update_one(clientModel, client_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
