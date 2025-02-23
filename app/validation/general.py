from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta


class ValidateServise:
    @classmethod
    async def validate_existence(cls, Model: DeclarativeMeta, id_field: str, data: BaseModel, session: AsyncSession):
        data_exists = await session.execute(select(Model).where(Model.id == getattr(data, id_field)))
        return data_exists.scalar_one_or_none() is not None
