from fastapi import HTTPException
from app.database import new_session

from sqlalchemy import select, delete,insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from pydantic import BaseModel

class GeneralOperations:
    @classmethod
    async def add_one(cls, Model: DeclarativeMeta, schema: BaseModel,session: AsyncSession):
        query = insert(Model).values(**schema.model_dump())
        result = await session.execute(query)  
        await session.commit()
        inserted_id = result.lastrowid
        return {"id": inserted_id, **schema.model_dump()}
    
    @classmethod
    async def get_all(cls, Model:DeclarativeMeta,session:AsyncSession):
        return (await session.scalars(select(Model))).all()

    @classmethod
    async def delete_one(cls, ID: int, Model:DeclarativeMeta,session:AsyncSession):
        query = delete(Model).where(Model.id == ID)
        result = await session.execute(query)
        await session.commit()
        if (result.rowcount == 0):
            raise HTTPException(status_code=404, detail=f"Not found")

    @classmethod
    async def get_one(cls, ID: int, Model):
        async with new_session() as session:
            query = select(Model).where(Model.id == ID)
            result = await session.execute(query)
            return result.scalar_one_or_none()
