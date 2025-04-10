from typing import List
from fastapi import APIRouter, Depends, Query,  status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import utils
from app.database import get_session
from app.schemas.client import ClientGetSchema
from app.schemas.pagination import PaginationSchema
from app.schemas.social_status import Social_StatusAddSchema, Social_StatusGetSchema, Social_StatusUpdateSchema
from app.repositories.status import StatusRepository

router_status = APIRouter(
    prefix="/social_statuses",
    tags=["status"]
)


# получение всех клиентов статуса
@router_status.get("/{status_id}/clients", status_code=status.HTTP_200_OK, response_model=PaginationSchema[ClientGetSchema])
async def get_status_clients(status_id: int,
                             _: bool = utils.role_required(["admin", "editor"]),
                             page: int = Query(1, ge=1),
                             per_page: int = Query(10, ge=1, le=100),
                             session: AsyncSession = Depends(get_session)):
    return await StatusRepository.get_clients(status_id, session, page, per_page)


# добавление статуса


@router_status.post("", status_code=status.HTTP_201_CREATED, response_model=Social_StatusGetSchema)
async def create_status(data: Social_StatusAddSchema,
                        _: bool = utils.role_required(["admin", "editor"]),
                        session: AsyncSession = Depends(get_session)):
    result = await StatusRepository.create(data, session)
    return result


# получение всех статусов
@router_status.get("", status_code=status.HTTP_200_OK, response_model=PaginationSchema[Social_StatusGetSchema])
async def get_statuses(_: bool = utils.role_required(["admin", "editor"]),
                       page: int = Query(1, ge=1),
                       per_page: int = Query(10, ge=1, le=100),
                       session: AsyncSession = Depends(get_session)):
    statuses = await StatusRepository.get_all(session, page, per_page)
    return statuses


# удаление статуса по id
@router_status.delete("/{status_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_status(status_id: int,
                        _: bool = utils.role_required(["admin", "editor"]),
                        session: AsyncSession = Depends(get_session)):
    await StatusRepository.delete(status_id,  session)
    return {"message": "Deleted successfully"}


# получение статуса по id
@router_status.get("/{status_id}", status_code=status.HTTP_200_OK, response_model=Social_StatusGetSchema)
async def get_status_by_id(status_id: int,
                           _: bool = utils.role_required(["admin", "editor"]),
                           session: AsyncSession = Depends(get_session)):
    result = await StatusRepository.get_one(status_id,  session)
    return result

# апдейт статуса по id


@router_status.put("/{status_id}", status_code=status.HTTP_200_OK, response_model=Social_StatusUpdateSchema)
async def update_status_by_id(status_id: int,
                              data: Social_StatusAddSchema,
                              _: bool = utils.role_required(["admin", "editor"]),
                              session: AsyncSession = Depends(get_session)):
    result = await StatusRepository.update(status_id, data, session)
    return result
