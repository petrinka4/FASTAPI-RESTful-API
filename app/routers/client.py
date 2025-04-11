
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import utils
from app.database import get_session
from app.schemas.account import AccountGetSchema
from app.schemas.client import ClientAddSchema, ClientGetSchema, ClientUpdateSchema
from app.repositories.client import ClientRepository
from app.schemas.pagination import PaginationSchema

router_client = APIRouter(
    prefix="/clients",
    tags=["client"]
)


# получение всех аккаунтов  клиента
@router_client.get("/{client_id}/accounts", status_code=status.HTTP_200_OK, response_model=PaginationSchema[AccountGetSchema])
async def get_client_accounts(client_id: int,
                              _: bool = utils.role_required(["admin", "editor"]),
                              page: int = Query(1, ge=1),
                              per_page: int = Query(10, ge=1, le=100),
                              session: AsyncSession = Depends(get_session)):
    return await ClientRepository.get_accounts(client_id, session, page, per_page)


# получение всех клиентов


@router_client.get("", status_code=status.HTTP_200_OK, response_model=PaginationSchema[ClientGetSchema])
async def get_clients(_: bool = utils.role_required(["admin", "editor"]),
                      page: int = Query(1, ge=1),
                      per_page: int = Query(10, ge=1, le=100),
                      session: AsyncSession = Depends(get_session)):
    clients = await ClientRepository.get_all(session, page, per_page)
    return clients

# добавление клиента


@router_client.post("", status_code=status.HTTP_201_CREATED, response_model=ClientGetSchema)
async def create_client(data: ClientAddSchema,
                        _: bool = utils.role_required(["admin", "editor"]),
                        session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.create(data, session)
    return result

# удаление клиента


@router_client.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: int,
                        _: bool = utils.role_required(["admin", "editor"]),
                        session: AsyncSession = Depends(get_session)):
    await ClientRepository.delete(client_id,  session)
    return {"message": "Deleted successfully"}

# получение клиента по id


@router_client.get("/{client_id}", status_code=status.HTTP_200_OK, response_model=ClientGetSchema)
async def get_client_by_id(client_id: int,
                           _: bool = utils.role_required(["admin", "editor"]),
                           session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.get_one(client_id,  session)
    return result

# апдейт клиента по id


@router_client.put("/{client_id}", status_code=status.HTTP_200_OK, response_model=ClientUpdateSchema)
async def update_client_by_id(client_id: int,
                              data: ClientAddSchema,
                              _: bool = utils.role_required(["admin", "editor"]),
                              session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.update(client_id, data, session)
    return result
