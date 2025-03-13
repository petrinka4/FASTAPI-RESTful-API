from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.branch import branchModel
from app.schemas.branch import BranchAddSchema
from app.resources.general import GeneralResources
from app.database import get_session

router_branch = APIRouter(
    prefix="/branch",
    tags=["branch"]
)

# получение всех филиалов


@router_branch.get("")
async def get_branches(session: AsyncSession = Depends(get_session)):
    try:
        branches = await GeneralResources.get_all(branchModel, session)
        return branches
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# добавление филиала


@router_branch.post("")
async def create_branch(data: BranchAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.create(branchModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# удаление филиала по id


@router_branch.delete("/{branch_id}")
async def delete_branch(branch_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete(branch_id, branchModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# получение филиала по id


@router_branch.get("/{branch_id}")
async def get_branch_by_id(branch_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(branch_id, branchModel, session)
        return result
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# апдейт филиала по id


@router_branch.put("/{branch_id}")
async def update_branch_by_id(branch_id: int, data: BranchAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.update(branchModel, branch_id, data, session)
        return {"status_code": 201, "message": "Updated successfully", "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))
