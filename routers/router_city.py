from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import CityAddSchema
from operations.cityOp import CityOperations

router_city=APIRouter(
    prefix="/cities",
    tags=["city"]
)

#добавление города
@router_city.post("")
async def add_city(data:Annotated[CityAddSchema,Depends()]):
    city_id=await CityOperations.add_one_city(data)
    return {"ok":True,"id":city_id}


  


#получение всех городов
@router_city.get("")
async def get_cities():
    cities=await CityOperations.get_all_cities()
    return cities




#удаление города по id
@router_city.delete("/{city_id}") 
async def delete_city(city_id:int):
    data=await CityOperations.delete_one_city(city_id)
    return data
      

#получение города по id
@router_city.get("/{city_id}")
async def get_city_by_id(city_id:int):
  data=await CityOperations.get_one_city(city_id)
  return data

#апдейт города по id
@router_city.put("/{city_id}")
async def update_city_by_id(city_id:int,data:Annotated[CityAddSchema,Depends()]):
    result=await CityOperations.update_city(city_id,data)
    return result

