from typing import Annotated
from fastapi import APIRouter, Depends

from models.accountModel import accountModel
from schemas import AccountAddSchema
from operations.accountOp import AccountOperations
from operations.generalOp import GeneralOperations

router_account=APIRouter(
    prefix="/accounts",
    tags=["account"]
)

#получение всех аккаунтов
@router_account.get("")
async def get_accounts():
    accounts=await GeneralOperations.get_all(accountModel)
    return accounts

#добавление аккаунта
@router_account.post("")
async def add_account(data: Annotated[AccountAddSchema, Depends()]):
    result = await AccountOperations.add_one_account(data)
    if isinstance(result, dict) and "error" in result:
        return {"ok": False, "error": result["error"]}
    return {"ok": True, "id": result}

#удаление аккаунта по id
@router_account.delete("/{account_id}") 
async def delete_account(account_id:int):
    data=await GeneralOperations.delete_one(account_id,accountModel)
    return data

#получение аккаунта по id
@router_account.get("/{account_id}")
async def get_account_by_id(account_id:int):
  data=await GeneralOperations.get_one(account_id,accountModel)
  return data

#апдейт аккаунта по id
@router_account.put("/{account_id}")
async def update_account_by_id(account_id:int,data:Annotated[AccountAddSchema,Depends()]):
    result=await AccountOperations.update_account(account_id,data)
    return result