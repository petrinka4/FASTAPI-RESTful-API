from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.social_status import Social_StatusAddSchema
from app.repositories.status import StatusRepository

router_status = APIRouter(
    prefix="/social_status",
    tags=["status"]
)

# добавление статуса


@router_status.post("", status_code=status.HTTP_201_CREATED)
async def create_status(data: Social_StatusAddSchema, session: AsyncSession = Depends(get_session)):
    result = await StatusRepository.create(data, session)
    return {"object": result}


# получение всех статусов
@router_status.get("", status_code=status.HTTP_200_OK)
async def get_statuses(session: AsyncSession = Depends(get_session)):
    statuses = await StatusRepository.get_all(session)
    return statuses


# удаление статуса по id
@router_status.delete("/{status_id}", status_code=status.HTTP_200_OK)
async def delete_status(status_id: int, session: AsyncSession = Depends(get_session)):
    await StatusRepository.delete(status_id,  session)
    return {"message": "Deleted successfully"}


# получение статуса по id
@router_status.get("/{status_id}", status_code=status.HTTP_200_OK)
async def get_status_by_id(status_id: int, session: AsyncSession = Depends(get_session)):
    result = await StatusRepository.get_one(status_id,  session)
    return result

# апдейт статуса по id


@router_status.put("/{status_id}", status_code=status.HTTP_200_OK)
async def update_status_by_id(status_id: int, data: Social_StatusAddSchema, session: AsyncSession = Depends(get_session)):
    result = await StatusRepository.update(status_id, data, session)
    return {"object": result}
