from fastapi import HTTPException
from app.schemas import BranchAddSchema
from app.validation.branch import validateBranch
from app.operations.general import GeneralOperations

from app.models.branch import branchModel
from app.models.bank import bankModel
from app.models.city import cityModel

from app.database import new_session

from sqlalchemy import select, text, update, insert
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel


class BranchOperations:

    @classmethod
    async def add_branch(cls, Model: DeclarativeMeta, data: BaseModel, session: AsyncSession):
        if (await validateBranch(data, session)):
            return await GeneralOperations.add_one(Model, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_branch(cls, branch_id, data: BranchAddSchema):
        async with new_session() as session:
            query = select(branchModel).where(branchModel.id == branch_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect branch_id"}
            query = select(bankModel).where(bankModel.id == data.bank_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect bank_id"}
            query = select(cityModel).where(cityModel.id == data.city_id)
            result = await session.execute(query)

            if (result.scalar_one_or_none() == None):
                return {"ok": False, "error": "Incorrect city_id"}
            query = update(branchModel).where(branchModel.id == branch_id).values(
                bank_id=data.bank_id, city_id=data.city_id)
            await session.execute(query)
            await session.commit()
            return {"ok": True}
