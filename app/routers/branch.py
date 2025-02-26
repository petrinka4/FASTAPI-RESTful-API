from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.branch import branchModel
from app.schemas import BranchAddSchema
from app.resources.branch import BranchResources
from app.resources.general import GeneralResources
from app.database import get_session

router_branch = APIRouter(
    prefix="/branch",
    tags=["branch"]
)

# получение всех филиалов


@router_branch.get("")
async def get_branches(session: AsyncSession = Depends(get_session)):
    branches = await GeneralResources.get_all(branchModel, session)
    return branches

# добавление филиала


@router_branch.post("")
async def add_branch(data: BranchAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await BranchResources.add_branch(data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# удаление филиала по id


@router_branch.delete("/{branch_id}")
async def delete_branch(branch_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete_one(branch_id, branchModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# получение филиала по id


@router_branch.get("/{branch_id}")
async def get_branch_by_id(branch_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(branch_id, branchModel, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# апдейт филиала по id


@router_branch.put("/{branch_id}")
async def update_branch_by_id(branch_id: int, data: BranchAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        await BranchResources.update_branch(branch_id, data, session)
        return {"status_code": 200, "message": "Updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
