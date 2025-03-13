from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.city import cityModel
from app.schemas.city import CityAddSchema
from app.resources.general import GeneralResources

router_city = APIRouter(
    prefix="/cities",
    tags=["city"]
)

# добавление города


@router_city.post("")
async def create_city(data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.create(cityModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# получение всех городов
@router_city.get("")
async def get_cities(session: AsyncSession = Depends(get_session)):
    try:
        cities = await GeneralResources.get_all(cityModel, session)
        return cities
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# удаление города по id
@router_city.delete("/{city_id}")
async def delete_city(city_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete(city_id, cityModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# получение города по id
@router_city.get("/{city_id}")
async def get_city_by_id(city_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(city_id, cityModel, session)
        return result
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# апдейт города по id


@router_city.put("/{city_id}")
async def update_city_by_id(city_id: int, data: CityAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.update(cityModel, city_id, data, session)
        return {"status_code": 201, "message": "Updated successfully", "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))
