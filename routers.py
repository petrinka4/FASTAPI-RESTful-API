from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import BankAddSchema,CityAddSchema
from repository import BankRepository,CityRepository

router_bank=APIRouter(
    prefix="/banks",
    tags=["bank"]
)


#добавление банка
@router_bank.post("")
async def add_bank(data:Annotated[BankAddSchema,Depends()]):
    bank_id=await BankRepository.add_one_bank(data)
    return {"ok":True,"id":bank_id}


  


#получение всех банков
@router_bank.get("")
async def get_banks():
    banks=await BankRepository.get_all_banks()
    return banks




#удаление банка по id
@router_bank.delete("/{bank_id}") 
async def delete_bank(bank_id:int):
    data=await BankRepository.delete_one_bank(bank_id)
    return data
      

#получение банка по id
@router_bank.get("/{bank_id}")
async def get_bank_by_id(bank_id:int):
  data=await BankRepository.get_one_bank(bank_id)
  return data

#апдейт банка по id
@router_bank.put("/{bank_id}")
async def update_bank_by_id(bank_id:int,data:Annotated[BankAddSchema,Depends()]):
    result=await BankRepository.update_bank(bank_id,data)
    return result


router_city=APIRouter(
    prefix="/cities",
    tags=["city"]
)

#добавление города
@router_city.post("")
async def add_city(data:Annotated[CityAddSchema,Depends()]):
    city_id=await CityRepository.add_one_city(data)
    return {"ok":True,"id":city_id}


  


#получение всех городов
@router_city.get("")
async def get_cities():
    cities=await CityRepository.get_all_cities()
    return cities




#удаление города по id
@router_city.delete("/{city_id}") 
async def delete_city(city_id:int):
    data=await CityRepository.delete_one_city(city_id)
    return data
      

#получение города по id
@router_city.get("/{city_id}")
async def get_city_by_id(city_id:int):
  data=await CityRepository.get_one_city(city_id)
  return data

#апдейт города по id
@router_city.put("/{city_id}")
async def update_city_by_id(city_id:int,data:Annotated[CityAddSchema,Depends()]):
    result=await CityRepository.update_city(city_id,data)
    return result