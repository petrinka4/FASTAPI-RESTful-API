from fastapi import HTTPException

from app.resources.general import GeneralResources
from app.models.social_status import social_statusModel
from app.validation.general import ValidateServise

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class StatusResources:
    @classmethod
    async def add_status(cls, data: BaseModel, session: AsyncSession):
        return await GeneralResources.add_one(social_statusModel, data, session)

    @classmethod
    async def update_status(cls,  status_id: int, data, session):
        if (await ValidateServise.validate_id_existence(social_statusModel, "id", status_id, session)):
            return await GeneralResources.update_one(social_statusModel, status_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
