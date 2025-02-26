from fastapi import HTTPException

from app.resources.general import GeneralResources
from app.models.city import cityModel
from app.validation.general import ValidateServise

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class CityResources:
    @classmethod
    async def add_city(cls, data: BaseModel, session: AsyncSession):
        return await GeneralResources.add_one(cityModel, data, session)

    @classmethod
    async def update_city(cls,  city_id: int, data, session):
        if (await ValidateServise.validate_id_existence(cityModel, "id", city_id, session)):
            return await GeneralResources.update_one(cityModel, city_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
