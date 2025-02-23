from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.account import accountModel
from app.schemas import AccountAddSchema
from app.operations.account import AccountOperations
from app.operations.general import GeneralOperations

router_account = APIRouter(
    prefix="/accounts",
    tags=["account"]
)

# получение всех аккаунтов


@router_account.get("")
async def get_accounts(session: AsyncSession = Depends(get_session)):
    accounts = await GeneralOperations.get_all(accountModel, session)
    return accounts

# добавление аккаунта


@router_account.post("")
async def add_branch(data: AccountAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await AccountOperations.add_account(accountModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# удаление аккаунта по id


@router_account.delete("/{account_id}")
async def delete_account(account_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralOperations.delete_one(account_id, accountModel,session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# получение аккаунта по id


@router_account.get("/{account_id}")
async def get_account_by_id(account_id: int):
    data = await GeneralOperations.get_one(account_id, accountModel)
    return data

# апдейт аккаунта по id


@router_account.put("/{account_id}")
async def update_account_by_id(account_id: int, data: Annotated[AccountAddSchema, Depends()]):
    result = await AccountOperations.update_account(account_id, data)
    return result
