from app.schemas import CityAddSchema
from app.models.cityModel import cityModel

from app.database import new_session
from sqlalchemy import select, text, update, insert, delete


class CityOperations:
    @classmethod
    async def add_one_city(cls, data: CityAddSchema):
        async with new_session() as session:
            query = (insert(cityModel)
                     .values(name=data.name))
            await session.execute(query)
            await session.commit()
            result = await session.execute(text("SELECT LAST_INSERT_ID()"))
            return result.scalar()

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
