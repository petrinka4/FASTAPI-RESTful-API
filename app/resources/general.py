from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from pydantic import BaseModel


class GeneralResources:
    @classmethod
    async def create(cls, Model: DeclarativeMeta, schema: BaseModel, session: AsyncSession):
        obj = Model(**schema.model_dump())
        session.add(obj)
        await session.commit()
        return obj

# сделал в несколько строчек для лучшей читаемости
    @classmethod
    async def get_all(cls, Model: DeclarativeMeta, session: AsyncSession):
        query = select(Model)
        result = await session.scalars(query)
        return result.all()

    @classmethod
    async def delete(cls, ID: int, Model: DeclarativeMeta, session: AsyncSession):
        obj = await session.get(Model, ID)
        if not obj:
            raise HTTPException(status_code=404, detail=f"Not found")
        await session.delete(obj)
        await session.commit()

    @classmethod
    async def get_one(cls, ID: int, Model: DeclarativeMeta, session: AsyncSession):
        return await session.get(Model, ID)

    @classmethod
    async def update(cls, Model: DeclarativeMeta, ID: int, schema: BaseModel, session: AsyncSession):
        obj = await session.get(Model, ID)
        if not obj:
            raise HTTPException(status_code=422, detail=f"Incorrect id")
        for key, value in schema.model_dump().items():
            setattr(obj, key, value)
        await session.commit()
        return obj
