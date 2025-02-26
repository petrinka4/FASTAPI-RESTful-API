
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.account import accountModel
from app.schemas import AccountAddSchema
from app.resources.account import AccountResources
from app.resources.general import GeneralResources

router_account = APIRouter(
    prefix="/accounts",
    tags=["account"]
)

# получение всех аккаунтов


@router_account.get("")
async def get_accounts(session: AsyncSession = Depends(get_session)):
    accounts = await GeneralResources.get_all(accountModel, session)
    return accounts

# добавление аккаунта


@router_account.post("")
async def add_account(data: AccountAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await AccountResources.add_account(data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# удаление аккаунта по id


@router_account.delete("/{account_id}")
async def delete_account(account_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete_one(account_id, accountModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# получение аккаунта по id


@router_account.get("/{account_id}")
async def get_account_by_id(account_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(account_id, accountModel, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# апдейт аккаунта по id


@router_account.put("/{account_id}")
async def update_account_by_id(account_id: int, data: AccountAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        await AccountResources.update_account(account_id, data, session)
        return {"status_code": 200, "message": "Updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
