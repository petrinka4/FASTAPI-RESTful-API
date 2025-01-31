from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import BankAddSchema
from operations.bankOp import BankOperations

router_bank=APIRouter(
    prefix="/banks",
    tags=["bank"]
)


#добавление банка
@router_bank.post("")
async def add_bank(data:Annotated[BankAddSchema,Depends()]):
    bank_id=await BankOperations.add_one_bank(data)
    return {"ok":True,"id":bank_id}


  


#получение всех банков
@router_bank.get("")
async def get_banks():
    banks=await BankOperations.get_all_banks()
    return banks




#удаление банка по id
@router_bank.delete("/{bank_id}") 
async def delete_bank(bank_id:int):
    data=await BankOperations.delete_one_bank(bank_id)
    return data
      

#получение банка по id
@router_bank.get("/{bank_id}")
async def get_bank_by_id(bank_id:int):
  data=await BankOperations.get_one_bank(bank_id)
  return data

#апдейт банка по id
@router_bank.put("/{bank_id}")
async def update_bank_by_id(bank_id:int,data:Annotated[BankAddSchema,Depends()]):
    result=await BankOperations.update_bank(bank_id,data)
    return result




