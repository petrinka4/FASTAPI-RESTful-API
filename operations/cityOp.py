from schemas import CityAddSchema
from models.cityModel import cityModel

from database import new_session
from sqlalchemy import select, update,insert,delete

class CityOperations:
    @classmethod
    async def add_one_city(cls,data:CityAddSchema):
        async with new_session() as session:
            query=(insert(cityModel)
                   .values(name=data.name)
                   .returning(cityModel.id))   
            result=await session.execute(query)
            await session.commit()
            return result.scalar()



    @classmethod
    async def update_city(cls,city_id,data:CityAddSchema):
        async with new_session() as session:
            query=select(cityModel).where(cityModel.id==city_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect city_id"}
            query=update(cityModel).where(cityModel.id==city_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok":True}

