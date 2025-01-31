from schemas import BankAddSchema,CityAddSchema
from models import bankModel,cityModel
from database import new_session
from sqlalchemy import select, update,insert,delete

class BankRepository:
    
    @classmethod
    async def add_one_bank(cls,data:BankAddSchema):
        async with new_session() as session:
            query=(insert(bankModel)
                   .values(name=data.name)
                   .returning(bankModel.id))   
            result=await session.execute(query)
            await session.commit()
            return result.scalar()



    @classmethod
    async def get_all_banks(cls):
        async with new_session() as session:
            query=select(bankModel)
            result=await session.execute(query)
            return result.scalars().all()
        
    

    @classmethod
    async def delete_one_bank(cls,bank_id:int):
        async with new_session() as session:
            query= delete(bankModel).where(bankModel.id==bank_id)
            result=await session.execute(query)
            await session.commit()
            if (result.rowcount>0):
                return {"ok":True}
            else:
                return {"error":"bank not found"},404
          

    @classmethod
    async def get_one_bank(cls,bank_id:int):
        async with new_session() as session:
           query=select(bankModel).where(bankModel.id==bank_id)
           result=await session.execute(query)
           return result.scalar_one_or_none()
           
    
    @classmethod
    async def update_bank(cls,bank_id,data:BankAddSchema):
        async with new_session() as session:
            query=update(bankModel).where(bankModel.id==bank_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok":True}


class CityRepository:
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
    async def get_all_cities(cls):
        async with new_session() as session:
            query=select(cityModel)
            result=await session.execute(query)
            return result.scalars().all()
        
    

    @classmethod
    async def delete_one_city(cls,city_id:int):
        async with new_session() as session:
            query= delete(cityModel).where(cityModel.id==city_id)
            result=await session.execute(query)
            await session.commit()
            if (result.rowcount>0):
                return {"ok":True}
            else:
                return {"error":"bank not found"},404
          

    @classmethod
    async def get_one_city(cls,city_id:int):
        async with new_session() as session:
           query=select(cityModel).where(cityModel.id==city_id)
           result=await session.execute(query)
           return result.scalar_one_or_none()
           
    
    @classmethod
    async def update_city(cls,city_id,data:CityAddSchema):
        async with new_session() as session:
            query=update(cityModel).where(cityModel.id==city_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok":True}














     