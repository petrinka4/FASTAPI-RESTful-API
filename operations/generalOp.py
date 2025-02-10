from database import new_session
from sqlalchemy import select, update,insert,delete

class GeneralOperations: 
    @classmethod
    async def get_all(cls,Model):
        async with new_session() as session:
            query=select(Model)
            result=await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def delete_one(cls,ID:int,Model):
        async with new_session() as session:
            query=delete(Model).where(Model.id==ID)
            result=await session.execute(query)
            await session.commit()
            if (result.rowcount>0):
                return {"ok":True}
            else:
                return {"ok":False,"error":"Not found"},404
            
    @classmethod
    async def get_one(cls,ID:int,Model):
        async with new_session() as session:
            query=select(Model).where(Model.id==ID)
            result=await session.execute(query)
            return result.scalar_one_or_none()