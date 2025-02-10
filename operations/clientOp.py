from schemas import ClientAddSchema
from models import clientModel,social_statusModel
from database import new_session
from sqlalchemy import select, update,insert,delete

class ClientOperations:

    @classmethod
    async def add_one_client(cls,client:ClientAddSchema):
        async with new_session() as session:
            query=(select(social_statusModel).where(social_statusModel.id==client.social_status_id))
            result = await session.execute(query)
            if (result.one_or_none()==None):
                return {"error":"Incorect social_status_id"}
            query=(insert(clientModel)
                   .values(name=client.name,social_status_id=client.social_status_id)
                   .returning(clientModel.id))
            result=await session.execute(query)
            await session.commit()
            return result.scalar()
        
        
    @classmethod
    async def update_client(cls,client_id:int,data:ClientAddSchema):
        async with new_session() as session:
            query=select(clientModel).where(clientModel.id==client_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect client_id"}
            query=select(social_statusModel).where(social_statusModel.id==data.social_status_id)
            result=await session.execute(query)

            if (result.scalar_one_or_none()==None):
                return {"ok":False,"error":"Incorrect social_status_id"}
           
            query=update(clientModel).where(clientModel.id==client_id).values(name=data.name,social_status_id=data.social_status_id)
            await session.execute(query)
            await session.commit()
            return {"ok":True}

            
            