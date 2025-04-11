from fastapi import HTTPException

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    Model: DeclarativeMeta = None

    @classmethod
    async def create(cls, schema: BaseModel, session: AsyncSession):
        obj = cls.Model(**schema.model_dump())
        session.add(obj)
        await session.commit()
        return obj

    @classmethod
    async def get_all(cls, session: AsyncSession, page: int = 1, per_page: int = 10):
        total_query = select(func.count()).select_from(cls.Model)
        total = (await session.execute(total_query)).scalar()

        total_pages = (total + per_page - 1) // per_page

        offset = (page - 1) * per_page
        query = select(cls.Model).offset(offset).limit(per_page)
        result = await session.scalars(query)
        items = result.all()

        return {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": total_pages,
            "data": items
        }

    @classmethod
    async def get_related(
        cls,
        session: AsyncSession,
        foreign_key_field,
        ID: int,
        page: int = 1,
        per_page: int = 10
    ):
        total_query = select(func.count()).select_from(cls.Model).where(foreign_key_field == ID)
        total = (await session.execute(total_query)).scalar_one()

        total_pages = (total + per_page - 1) // per_page
        offset = (page - 1) * per_page

        query = (
            select(cls.Model)
            .where(foreign_key_field == ID)
            .offset(offset)
            .limit(per_page)
        )
        result = await session.scalars(query)
        items = result.all()

        return {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": total_pages,
            "data": items
        }

    @classmethod
    async def delete(cls, ID: int, session: AsyncSession):
        obj = await session.get(cls.Model, ID)
        if not obj:
            raise HTTPException(status_code=404, detail=f"Not found")
        await session.delete(obj)
        await session.commit()

    @classmethod
    async def get_one(cls, ID: int, session: AsyncSession):
        return await session.get(cls.Model, ID)

    @classmethod
    async def update(cls, ID: int, schema: BaseModel, session: AsyncSession):
        obj = await session.get(cls.Model, ID)
        if not obj:
            raise HTTPException(status_code=422, detail=f"Incorrect id")
        for key, value in schema.model_dump().items():
            setattr(obj, key, value)
        await session.commit()
        return obj
