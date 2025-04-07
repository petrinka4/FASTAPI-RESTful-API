
from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.bank import BankAddSchema, BankGetSchema, BankUpdateSchema
from app.schemas.account import AccountGetSchema
from app.schemas.pagination import PaginationSchema
from app.repositories.bank import BankRepository
from app.schemas.branch import BranchGetSchema

router_bank = APIRouter(
    prefix="/banks",
    tags=["bank"]
)


# получение всех аккаунтов  банка
@router_bank.get("/{bank_id}/accounts", status_code=status.HTTP_200_OK, response_model=PaginationSchema[AccountGetSchema])
async def get_bank_accounts(bank_id: int,
                            page: int = Query(1, ge=1),
                            per_page: int = Query(10, ge=1, le=100),
                            session: AsyncSession = Depends(get_session)):
    return await BankRepository.get_accounts(bank_id, session, page, per_page)

# получение всех филиалов  банка


@router_bank.get("/{bank_id}/branches", status_code=status.HTTP_200_OK, response_model=PaginationSchema[BranchGetSchema])
async def get_bank_branches(bank_id: int,
                            page: int = Query(1, ge=1),
                            per_page: int = Query(10, ge=1, le=100),
                            session: AsyncSession = Depends(get_session)):
    return await BankRepository.get_branches(bank_id, session, page, per_page)


@router_bank.post("", status_code=status.HTTP_201_CREATED, response_model=BankGetSchema)
async def create_bank(data: BankAddSchema, session: AsyncSession = Depends(get_session)):
    result = await BankRepository.create(data, session)
    return result


# получение всех банков
@router_bank.get("", status_code=status.HTTP_200_OK, response_model=PaginationSchema[BankGetSchema])
async def get_banks(page: int = Query(1, ge=1),
                    per_page: int = Query(10, ge=1, le=100),
                    session: AsyncSession = Depends(get_session)
                    ):
    banks = await BankRepository.get_all(session, page, per_page)
    return banks


# удаление банка по id
@router_bank.delete("/{bank_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank(bank_id: int, session: AsyncSession = Depends(get_session)):
    await BankRepository.delete(bank_id,  session)
    return {"message": "Deleted successfully"}


# получение банка по id
@router_bank.get("/{bank_id}", status_code=status.HTTP_200_OK, response_model=BankGetSchema)
async def get_bank_by_id(bank_id: int, session: AsyncSession = Depends(get_session)):
    result = await BankRepository.get_one(bank_id,  session)
    return result

# апдейт банка по id


@router_bank.put("/{bank_id}", status_code=status.HTTP_200_OK, response_model=BankUpdateSchema)
async def update_bank_by_id(bank_id: int, data: BankAddSchema, session: AsyncSession = Depends(get_session)):
    result = await BankRepository.update(bank_id, data, session)
    return result
