from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.city import cityModel
from app.schemas import CityAddSchema
from app.operations.city import CityOperations
from app.operations.general import GeneralOperations

router_city = APIRouter(
    prefix="/cities",
    tags=["city"]
)

# добавление города


@router_city.post("")
async def add_city(data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await CityOperations.add_city(cityModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")


# получение всех городов
@router_city.get("")
async def get_cities(session: AsyncSession = Depends(get_session)):
    cities = await GeneralOperations.get_all(cityModel, session)
    return cities


# удаление города по id
@router_city.delete("/{city_id}")
async def delete_city(city_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralOperations.delete_one(city_id, cityModel,session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")


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
