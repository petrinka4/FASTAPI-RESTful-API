
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.client import clientModel
from app.schemas import ClientAddSchema
from app.resources.client import ClientResources
from app.resources.general import GeneralResources

router_client = APIRouter(
    prefix="/clients",
    tags=["client"]
)

# получение всех клиентов


@router_client.get("")
async def get_clients(session: AsyncSession = Depends(get_session)):
    clients = await GeneralResources.get_all(clientModel, session)
    return clients

# добавление клиента


@router_client.post("")
async def add_client(data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await ClientResources.add_client(data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# удаление клиента


@router_client.delete("/{client_id}")
async def delete_client(client_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete_one(client_id, clientModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# получение клиента по id


@router_client.get("/{client_id}")
async def get_client_by_id(client_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(client_id, clientModel, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# апдейт клиента по id


@router_client.put("/{client_id}")
async def update_client_by_id(client_id: int, data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        await ClientResources.update_client(client_id, data, session)
        return {"status_code": 200, "message": "Updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
