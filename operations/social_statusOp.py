from schemas import Social_StatusAddSchema
from models import social_statusModel
from database import new_session
from sqlalchemy import select, update,insert,delete

class StatusOperations:
    @classmethod
    async def add_one_status(cls,data:Social_StatusAddSchema):
        async with new_session() as session:
            query=(insert(social_statusModel)
                   .values(name=data.name)
                   .returning(social_statusModel.id))   
            result=await session.execute(query)
            await session.commit()
            return result.scalar()



    @classmethod
    async def get_all_statuses(cls):
        async with new_session() as session:
            query=select(social_statusModel)
            result=await session.execute(query)
            return result.scalars().all()
        
    

    @classmethod
    async def delete_one_status(cls,status_id:int):
        async with new_session() as session:
            query= delete(social_statusModel).where(social_statusModel.id==status_id)
            result=await session.execute(query)
            await session.commit()
            if (result.rowcount>0):
                return {"ok":True}
            else:
                return {"error":"status not found"},404
          

    @classmethod
    async def get_one_status(cls,status_id:int):
        async with new_session() as session:
           query=select(social_statusModel).where(social_statusModel.id==status_id)
           result=await session.execute(query)
           return result.scalar_one_or_none()
           
    
    @classmethod
    async def update_status(cls,status_id,data:Social_StatusAddSchema):
        async with new_session() as session:
            query=select(social_statusModel).where(social_statusModel.id==status_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect status_id"}
            query=update(social_statusModel).where(social_statusModel.id==status_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok":True}

