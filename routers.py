from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import BankAddSchema
from repository import BankRepository

router=APIRouter()


#добавление банка
@router.post("/banks")
async def add_bank(data:Annotated[BankAddSchema,Depends()]):
    bank_id=await BankRepository.add_one_bank(data)
    return {"ok":True,"id":bank_id}


  


#получение всех банков
@router.get("/banks")
async def get_banks():
    banks=await BankRepository.get_all_banks()
    return banks




#удаление банка по id
@router.delete("/banks/{bank_id}") 
async def delete_bank(bank_id:int):
    data=await BankRepository.delete_one_bank(bank_id)
    return data
      

#получение банка по id
@router.get("/banks/{bank_id}")
async def get_bank_by_id(bank_id:int):
  data=await BankRepository.get_one_bank(bank_id)
  return data

#апдейт банка по id
@router.put("/banks/{bank_id}")
async def update_bank_by_id(bank_id:int,data:Annotated[BankAddSchema,Depends()]):
    result=await BankRepository.update_bank(bank_id,data)
    return result