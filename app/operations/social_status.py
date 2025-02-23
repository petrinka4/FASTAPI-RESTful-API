from app.operations.general import GeneralOperations
from app.schemas import Social_StatusAddSchema

from app.models.social_status import social_statusModel

from app.database import new_session

from sqlalchemy import select, text, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from pydantic import BaseModel


class StatusOperations:
    @classmethod
    async def add_status(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        return await GeneralOperations.add_one(Model, data, session)
        

    @classmethod
    async def update_status(cls, status_id, data: Social_StatusAddSchema):
        async with new_session() as session:
            query = select(social_statusModel).where(
                social_statusModel.id == status_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect status_id"}
            query = update(social_statusModel).where(
                social_statusModel.id == status_id).values(name=data.name)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
