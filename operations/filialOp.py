from schemas import FilialAddSchema
from models import filialModel,bankModel,cityModel
from database import new_session
from sqlalchemy import select, update,insert,delete

class FilialOperations: 

  
    @classmethod
    async def add_one_filial(cls,data:FilialAddSchema):
        async with new_session() as session:
            query=select(bankModel).where(bankModel.id==data.bank_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"error":"Incorrect bank_id"}
            query=select(cityModel).where(cityModel.id==data.city_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"error":"Incorrect city_id"}
            query=(insert(filialModel)
                   .values(bank_id=data.bank_id,city_id=data.city_id)
                   .returning(filialModel.id))
            result=await session.execute(query)
            await session.commit()
            return result.scalar()
        
   
    @classmethod
    async def update_filial(cls,filial_id,data:FilialAddSchema):
        async with new_session() as session:
            query=select(filialModel).where(filialModel.id==filial_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect filial_id"}
            query=select(bankModel).where(bankModel.id==data.bank_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect bank_id"}
            query=select(cityModel).where(cityModel.id==data.city_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect city_id"}
            query=update(filialModel).where(filialModel.id==filial_id).values(bank_id=data.bank_id,city_id=data.city_id)
            await session.execute(query)
            await session.commit()
            return {"ok":True}
