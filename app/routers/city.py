from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.city import CityAddSchema
from app.repositories.city import CityRepository

router_city = APIRouter(
    prefix="/cities",
    tags=["city"]
)

# добавление города


@router_city.post("", status_code=status.HTTP_201_CREATED)
async def create_city(data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    result = await CityRepository.create(data, session)
    return {"object": result}


# получение всех городов
@router_city.get("", status_code=status.HTTP_200_OK)
async def get_cities(session: AsyncSession = Depends(get_session)):
    cities = await CityRepository.get_all(session)
    return cities


# удаление города по id
@router_city.delete("/{city_id}", status_code=status.HTTP_200_OK)
async def delete_city(city_id: int, session: AsyncSession = Depends(get_session)):
    await CityRepository.delete(city_id,  session)
    return {"message": "Deleted successfully"}


# получение города по id
@router_city.get("/{city_id}", status_code=status.HTTP_200_OK)
async def get_city_by_id(city_id: int, session: AsyncSession = Depends(get_session)):
    result = await CityRepository.get_one(city_id,  session)
    return result

# апдейт города по id


@router_city.put("/{city_id}", status_code=status.HTTP_200_OK)
async def update_city_by_id(city_id: int, data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    result = await CityRepository.update(city_id, data, session)
    return {"object": result}
