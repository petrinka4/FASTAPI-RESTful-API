from app.schemas import ClientAddSchema
from app.models.clientModel import clientModel
from app.models.social_statusModel import social_statusModel
from app.database import new_session
from sqlalchemy import select, text, update, insert, delete


class ClientOperations:

    @classmethod
    async def add_one_client(cls, client: ClientAddSchema):
        async with new_session() as session:
            query = (select(social_statusModel).where(
                social_statusModel.id == client.social_status_id))
            result = await session.execute(query)
            if (result.one_or_none() == None):
                return {"error": "Incorect social_status_id"}
            query = (insert(clientModel)
                     .values(name=client.name, social_status_id=client.social_status_id))
            await session.execute(query)
            await session.commit()
            result = await session.execute(text("SELECT LAST_INSERT_ID()"))
            return result.scalar()

    @classmethod
    async def update_client(cls, client_id: int, data: ClientAddSchema):
        async with new_session() as session:
            query = select(clientModel).where(clientModel.id == client_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect client_id"}
            query = select(social_statusModel).where(
                social_statusModel.id == data.social_status_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect social_status_id"}

            query = update(clientModel).where(clientModel.id == client_id).values(
                name=data.name, social_status_id=data.social_status_id)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
