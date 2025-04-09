from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import utils
from app.schemas.branch import BranchAddSchema, BranchGetSchema, BranchUpdateSchema
from app.repositories.branch import BranchRepository
from app.database import get_session
from app.schemas.pagination import PaginationSchema

router_branch = APIRouter(
    prefix="/branches",
    tags=["branch"]
)

# получение всех филиалов


@router_branch.get("", status_code=status.HTTP_200_OK, response_model=PaginationSchema[BranchGetSchema])
async def get_branches(_: None = Depends(utils.is_user_access),
                       page: int = Query(1, ge=1),
                       per_page: int = Query(10, ge=1, le=100),
                       session: AsyncSession = Depends(get_session)):
    branches = await BranchRepository.get_all(session, page, per_page)
    return branches


# добавление филиала


@router_branch.post("", status_code=status.HTTP_201_CREATED, response_model=BranchGetSchema)
async def create_branch(data: BranchAddSchema,
                        _: None = Depends(utils.is_editor_access),
                        session: AsyncSession = Depends(get_session)):
    result = await BranchRepository.create(data, session)
    return result

# удаление филиала по id


@router_branch.delete("/{branch_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_branch(branch_id: int,
                        _: None = Depends(utils.is_editor_access),
                        session: AsyncSession = Depends(get_session)):
    await BranchRepository.delete(branch_id,  session)
    return {"message": "Deleted successfully"}

# получение филиала по id


@router_branch.get("/{branch_id}", status_code=status.HTTP_200_OK, response_model=BranchGetSchema)
async def get_branch_by_id(branch_id: int, _: None = Depends(utils.is_editor_access),
                           session: AsyncSession = Depends(get_session)):
    result = await BranchRepository.get_one(branch_id,  session)
    return result

# апдейт филиала по id


@router_branch.put("/{branch_id}", status_code=status.HTTP_200_OK, response_model=BranchUpdateSchema)
async def update_branch_by_id(branch_id: int,
                              data: BranchAddSchema,
                              _: None = Depends(utils.is_editor_access),
                              session: AsyncSession = Depends(get_session)):
    result = await BranchRepository.update(branch_id, data, session)
    return result
