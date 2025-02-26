from fastapi import HTTPException

from app.validation.branch import validateBranch
from app.resources.general import GeneralResources
from app.models.branch import branchModel
from app.validation.general import ValidateServise

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class BranchResources:

    @classmethod
    async def add_branch(cls, data: BaseModel, session: AsyncSession):
        if (await validateBranch(data, session)):
            return await GeneralResources.add_one(branchModel, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_branch(cls,  branch_id: int, data, session):
        if (await validateBranch(data, session) and await ValidateServise.validate_id_existence(branchModel, "id", branch_id, session)):
            return await GeneralResources.update_one(branchModel, branch_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
