from schemas import Social_StatusAddSchema
from models.social_statusModel import social_statusModel
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

