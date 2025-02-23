from fastapi import HTTPException
from app.operations.general import GeneralOperations
from app.schemas import ClientAddSchema

from app.models.client import clientModel
from app.models.social_status import social_statusModel

from app.database import new_session

from sqlalchemy import select, text, update, insert, delete
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from app.validation.client import validateClient


class ClientOperations:

    @classmethod
    async def add_client(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        if (await validateClient(data, session)):
            return await GeneralOperations.add_one(Model, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_client(cls, client_id: int, data: ClientAddSchema):
        async with new_session() as session:
            query = select(clientModel).where(clientModel.id == client_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect client_id"}
            query = select(social_statusModel).where(
                social_statusModel.id == data.social_status_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect social_status_id"}

            query = update(clientModel).where(clientModel.id == client_id).values(
                name=data.name, social_status_id=data.social_status_id)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
