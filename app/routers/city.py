from typing import List
from fastapi import APIRouter, Depends,  status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.branch import BranchGetSchema
from app.schemas.city import CityAddSchema, CityGetSchema, CityUpdateSchema
from app.repositories.city import CityRepository

router_city = APIRouter(
    prefix="/cities",
    tags=["city"]
)



# получение всех филиалов города
@router_city.get("/{city_id}/branches", status_code=status.HTTP_200_OK, response_model=List[BranchGetSchema])
async def get_city_branches(city_id: int, session: AsyncSession = Depends(get_session)):
    return await CityRepository.get_branches(city_id, session)



# добавление города


@router_city.post("", status_code=status.HTTP_201_CREATED, response_model=CityGetSchema)
async def create_city(data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    result = await CityRepository.create(data, session)
    return result


# получение всех городов
@router_city.get("", status_code=status.HTTP_200_OK, response_model=List[CityGetSchema])
async def get_cities(session: AsyncSession = Depends(get_session)):
    cities = await CityRepository.get_all(session)
    return cities


# удаление города по id
@router_city.delete("/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(city_id: int, session: AsyncSession = Depends(get_session)):
    await CityRepository.delete(city_id,  session)
    return {"message": "Deleted successfully"}


# получение города по id
@router_city.get("/{city_id}", status_code=status.HTTP_200_OK, response_model=CityGetSchema)
async def get_city_by_id(city_id: int, session: AsyncSession = Depends(get_session)):
    result = await CityRepository.get_one(city_id,  session)
    return result

# апдейт города по id


@router_city.put("/{city_id}", status_code=status.HTTP_200_OK, response_model=CityUpdateSchema)
async def update_city_by_id(city_id: int, data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    result = await CityRepository.update(city_id, data, session)
    return result
