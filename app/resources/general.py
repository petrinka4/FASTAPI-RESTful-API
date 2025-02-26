from fastapi import HTTPException

from sqlalchemy import select, delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from pydantic import BaseModel


class GeneralResources:
    @classmethod
    async def add_one(cls, Model: DeclarativeMeta, schema: BaseModel, session: AsyncSession):
        query = insert(Model).values(**schema.model_dump())
        result = await session.execute(query)
        await session.commit()
        inserted_id = result.lastrowid
        return {"id": inserted_id, **schema.model_dump()}

    @classmethod
    async def get_all(cls, Model: DeclarativeMeta, session: AsyncSession):
        return (await session.scalars(select(Model))).all()

    @classmethod
    async def delete_one(cls, ID: int, Model: DeclarativeMeta, session: AsyncSession):
        query = delete(Model).where(Model.id == ID)
        result = await session.execute(query)
        await session.commit()
        if (result.rowcount == 0):
            raise HTTPException(status_code=404, detail=f"Not found")

    @classmethod
    async def get_one(cls, ID: int, Model: DeclarativeMeta, session: AsyncSession):
        return (await session.scalar(select(Model).where(Model.id == ID)))

    @classmethod
    async def update_one(cls, Model: DeclarativeMeta, id: int, schema: BaseModel, session: AsyncSession):
        query = update(Model).where(
            Model.id == id).values(**schema.model_dump())
        result = await session.execute(query)
        await session.commit()
        inserted_id = result.lastrowid
        return {"id": inserted_id, **schema.model_dump()}
