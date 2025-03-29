
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.account import AccountGetSchema
from app.schemas.client import ClientAddSchema, ClientGetSchema, ClientUpdateSchema
from app.repositories.client import ClientRepository

router_client = APIRouter(
    prefix="/clients",
    tags=["client"]
)


# получение всех аккаунтов  клиента
@router_client.get("/{client_id}/accounts", status_code=status.HTTP_200_OK, response_model=List[AccountGetSchema])
async def get_client_accounts(client_id: int, session: AsyncSession = Depends(get_session)):
    return await ClientRepository.get_accounts(client_id, session)


# получение всех клиентов


@router_client.get("", status_code=status.HTTP_200_OK, response_model=List[ClientGetSchema])
async def get_clients(session: AsyncSession = Depends(get_session)):
    clients = await ClientRepository.get_all(session)
    return clients

# добавление клиента


@router_client.post("", status_code=status.HTTP_201_CREATED, response_model=ClientGetSchema)
async def create_client(data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.create(data, session)
    return result

# удаление клиента


@router_client.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: int, session: AsyncSession = Depends(get_session)):
    await ClientRepository.delete(client_id,  session)
    return {"message": "Deleted successfully"}

# получение клиента по id


@router_client.get("/{client_id}", status_code=status.HTTP_200_OK, response_model=ClientGetSchema)
async def get_client_by_id(client_id: int, session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.get_one(client_id,  session)
    return result

# апдейт клиента по id


@router_client.put("/{client_id}", status_code=status.HTTP_200_OK, response_model=ClientUpdateSchema)
async def update_client_by_id(client_id: int, data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.update(client_id, data, session)
    return result
