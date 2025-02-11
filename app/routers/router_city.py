from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.cityModel import cityModel
from app.schemas import CityAddSchema
from app.operations.cityOp import CityOperations
from app.operations.generalOp import GeneralOperations

router_city = APIRouter(
    prefix="/cities",
    tags=["city"]
)

# добавление города


@router_city.post("")
async def add_city(data: Annotated[CityAddSchema, Depends()]):
    city_id = await CityOperations.add_one_city(data)
    return {"ok": True, "id": city_id}


# получение всех городов
@router_city.get("")
async def get_cities():
    cities = await GeneralOperations.get_all(cityModel)
    return cities


# удаление города по id
@router_city.delete("/{city_id}")
async def delete_city(city_id: int):
    data = await GeneralOperations.delete_one(city_id, cityModel)
    return data


# получение города по id
@router_city.get("/{city_id}")
async def get_city_by_id(city_id: int):
    data = await GeneralOperations.get_one(city_id, cityModel)
    return data

# апдейт города по id


@router_city.put("/{city_id}")
async def update_city_by_id(city_id: int, data: Annotated[CityAddSchema, Depends()]):
    result = await CityOperations.update_city(city_id, data)
    return result
