from schemas import BankAddSchema
from models import bankModel
from database import new_session
from sqlalchemy import select, update

class BankRepository:
    @classmethod
    async def add_one_bank(cls,data:BankAddSchema):
        async with new_session() as session:
          bank_dict=data.model_dump()  

          new_bank=bankModel(**bank_dict)
          session.add(new_bank)
          await session.commit()
          return new_bank.id
        


    @classmethod
    async def get_all_banks(cls):
        async with new_session() as session:
            query=select(bankModel)
            result=await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def delete_one_bank(cls,bank_id:int):
        async with new_session() as session:
            bank_del= await session.get(bankModel,bank_id)
            if bank_del:
                await session.delete(bank_del)
                await session.commit()
                return {"ok":True}
            return {"error":"Bank not found"}, 404 

    @classmethod
    async def get_one_bank(cls,bank_id:int):
        async with new_session() as session:
           bank=await session.get(bankModel,bank_id)
        if bank:
            return bank
        return {"error":"Bank not found"},404 
    
    @classmethod
    async def update_bank(cls,bank_id,data:BankAddSchema):
        async with new_session() as session:
            query=update(bankModel).where(bankModel.id==bank_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok":True}

















     