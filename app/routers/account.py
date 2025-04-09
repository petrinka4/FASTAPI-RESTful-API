
from typing import List
from fastapi import APIRouter, Depends, Query,  status
from sqlalchemy.ext.asyncio import AsyncSession


from app.auth import utils
from app.database import get_session
from app.repositories.account import AccountRepository
from app.schemas.account import AccountAddSchema, AccountGetSchema, AccountUpdateSchema
from app.schemas.bank import BankGetSchema
from app.schemas.card import CardGetSchema
from app.schemas.client import ClientGetSchema
from app.schemas.pagination import PaginationSchema


router_account = APIRouter(
    prefix="/accounts",
    tags=["account"]
)


# получение всех карт аккаунта
@router_account.get("/{account_id}/cards", status_code=status.HTTP_200_OK, response_model=PaginationSchema[CardGetSchema])
async def get_account_cards(account_id: int,
                            _: None = Depends(utils.is_editor_access),
                            page: int = Query(1, ge=1),
                            per_page: int = Query(10, ge=1, le=100),
                            session: AsyncSession = Depends(get_session)
                            ):
    return await AccountRepository.get_cards(account_id, session, page, per_page)

# получение всех аккаунтов


@router_account.get("", status_code=status.HTTP_200_OK, response_model=PaginationSchema[AccountGetSchema])
async def get_accounts(_: None = Depends(utils.is_editor_access),
                       page: int = Query(1, ge=1),
                       per_page: int = Query(10, ge=1, le=100),
                       session: AsyncSession = Depends(get_session)):
    accounts = await AccountRepository.get_all(session, page, per_page)
    return accounts

# добавление аккаунта


@router_account.post("", status_code=status.HTTP_201_CREATED, response_model=AccountGetSchema)
async def create_account(data: AccountAddSchema,
                         _: None = Depends(utils.is_user_access),
                         session: AsyncSession = Depends(get_session)):
    result = await AccountRepository.create(data, session)
    return result

# удаление аккаунта по id


@router_account.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(account_id: int,
                         _: None = Depends(utils.is_editor_access),
                         session: AsyncSession = Depends(get_session)):
    await AccountRepository.delete(account_id, session)
    return {"message": "Deleted successfully"}


# получение аккаунта по id


@router_account.get("/{account_id}", status_code=status.HTTP_200_OK, response_model=AccountGetSchema)
async def get_account_by_id(account_id: int,
                            _: None = Depends(utils.is_editor_access),
                            session: AsyncSession = Depends(get_session)):
    result = await AccountRepository.get_one(account_id, session)
    return result


# апдейт аккаунта по id


@router_account.put("/{account_id}", status_code=status.HTTP_200_OK, response_model=AccountUpdateSchema)
async def update_account_by_id(account_id: int,
                               data: AccountAddSchema,
                               _: None = Depends(utils.is_editor_access),
                               session: AsyncSession = Depends(get_session)):
    result = await AccountRepository.update(account_id, data, session)
    return result
