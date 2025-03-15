
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.client import ClientAddSchema
from app.repositories.client import ClientRepository

router_client = APIRouter(
    prefix="/clients",
    tags=["client"]
)

# получение всех клиентов


@router_client.get("", status_code=status.HTTP_200_OK)
async def get_clients(session: AsyncSession = Depends(get_session)):
    clients = await ClientRepository.get_all(session)
    return clients

# добавление клиента


@router_client.post("", status_code=status.HTTP_201_CREATED)
async def create_client(data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.create(data, session)
    return {"object": result}

# удаление клиента


@router_client.delete("/{client_id}", status_code=status.HTTP_200_OK)
async def delete_client(client_id: int, session: AsyncSession = Depends(get_session)):
    await ClientRepository.delete(client_id,  session)
    return {"message": "Deleted successfully"}

# получение клиента по id


@router_client.get("/{client_id}", status_code=status.HTTP_200_OK)
async def get_client_by_id(client_id: int, session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.get_one(client_id,  session)
    return result

# апдейт клиента по id


@router_client.put("/{client_id}", status_code=status.HTTP_200_OK)
async def update_client_by_id(client_id: int, data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    result = await ClientRepository.update(client_id, data, session)
    return {"object": result}
