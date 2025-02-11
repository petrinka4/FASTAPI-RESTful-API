from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.bankModel import bankModel
from app.schemas import BankAddSchema
from app.operations.bankOp import BankOperations
from app.operations.generalOp import GeneralOperations

router_bank = APIRouter(
    prefix="/banks",
    tags=["bank"]
)


# добавление банка
@router_bank.post("")
async def add_bank(data: Annotated[BankAddSchema, Depends()]):
    bank_id = await BankOperations.add_one_bank(data)
    return {"ok": True, "id": bank_id}


# получение всех банков
@router_bank.get("")
async def get_banks():
    banks = await GeneralOperations.get_all(bankModel)
    return banks


# удаление банка по id
@router_bank.delete("/{bank_id}")
async def delete_bank(bank_id: int):
    data = await GeneralOperations.delete_one(bank_id, bankModel)
    return data


# получение банка по id
@router_bank.get("/{bank_id}")
async def get_bank_by_id(bank_id: int):
    data = await GeneralOperations.get_one(bank_id, bankModel)
    return data

# апдейт банка по id


@router_bank.put("/{bank_id}")
async def update_bank_by_id(bank_id: int, data: Annotated[BankAddSchema, Depends()]):
    result = await BankOperations.update_bank(bank_id, data)
    return result
