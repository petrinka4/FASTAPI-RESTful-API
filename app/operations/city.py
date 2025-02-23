from app.operations.general import GeneralOperations
from app.schemas import CityAddSchema

from app.models.city import cityModel

from app.database import new_session

from sqlalchemy import select, text, update, insert
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel


class CityOperations:
    @classmethod
    async def add_city(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        return await GeneralOperations.add_one(Model, data, session)

    @classmethod
    async def update_city(cls, city_id, data: CityAddSchema):
        async with new_session() as session:
            query = select(cityModel).where(cityModel.id == city_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect city_id"}
            query = update(cityModel).where(
                cityModel.id == city_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
