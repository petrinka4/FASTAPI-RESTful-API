from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.branch import branchModel
from app.schemas import BranchAddSchema
from app.operations.branch import BranchOperations
from app.operations.general import GeneralOperations
from app.database import get_session

router_branch = APIRouter(
    prefix="/branch",
    tags=["branch"]
)

# получение всех филиалов


@router_branch.get("")
async def get_branches(session: AsyncSession = Depends(get_session)):
    branches = await GeneralOperations.get_all(branchModel, session)
    return branches

# добавление филиала


@router_branch.post("")
async def add_branch(data: BranchAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await BranchOperations.add_branch(branchModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# удаление филиала по id


@router_branch.delete("/{branch_id}")
async def delete_branch(branch_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralOperations.delete_one(branch_id, branchModel,session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# получение филиала по id


@router_branch.get("/{branch_id}")
async def get_branch_by_id(branch_id: int):
    data = await GeneralOperations.get_one(branch_id, branchModel)
    return data

# апдейт филиала по id


@router_branch.put("/{branch_id}")
async def update_branch_by_id(branch_id: int, data: Annotated[BranchAddSchema, Depends()]):
    result = await BranchOperations.update_branch(branch_id, data)
    return result
