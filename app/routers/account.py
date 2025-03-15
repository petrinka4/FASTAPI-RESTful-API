
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database import get_session
from app.repositories.account import AccountRepository
from app.schemas.account import AccountAddSchema


router_account = APIRouter(
    prefix="/accounts",
    tags=["account"]
)

# получение всех аккаунтов


@router_account.get("", status_code=status.HTTP_200_OK)
async def get_accounts(session: AsyncSession = Depends(get_session)):
    accounts = await AccountRepository.get_all(session)
    return accounts

# добавление аккаунта


@router_account.post("", status_code=status.HTTP_201_CREATED)
async def create_account(data: AccountAddSchema, session: AsyncSession = Depends(get_session)):
    result = await AccountRepository.create(data, session)
    return {"object": result}

# удаление аккаунта по id


@router_account.delete("/{account_id}", status_code=status.HTTP_200_OK)
async def delete_account(account_id: int, session: AsyncSession = Depends(get_session)):
    await AccountRepository.delete(account_id, session)
    return {"message": "Deleted successfully"}


# получение аккаунта по id


@router_account.get("/{account_id}", status_code=status.HTTP_200_OK)
async def get_account_by_id(account_id: int, session: AsyncSession = Depends(get_session)):
    result = await AccountRepository.get_one(account_id, session)
    return result


# апдейт аккаунта по id


@router_account.put("/{account_id}", status_code=status.HTTP_200_OK)
async def update_account_by_id(account_id: int, data: AccountAddSchema, session: AsyncSession = Depends(get_session)):
    result = await AccountRepository.update(account_id, data, session)
    return {"object": result}
