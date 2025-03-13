
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.client import clientModel
from app.schemas.client import ClientAddSchema
from app.resources.general import GeneralResources

router_client = APIRouter(
    prefix="/clients",
    tags=["client"]
)

# получение всех клиентов


@router_client.get("")
async def get_clients(session: AsyncSession = Depends(get_session)):
    try:
        clients = await GeneralResources.get_all(clientModel, session)
        return clients
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# добавление клиента


@router_client.post("")
async def create_client(data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.create(clientModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# удаление клиента


@router_client.delete("/{client_id}")
async def delete_client(client_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete(client_id, clientModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# получение клиента по id


@router_client.get("/{client_id}")
async def get_client_by_id(client_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(client_id, clientModel, session)
        return result
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# апдейт клиента по id


@router_client.put("/{client_id}")
async def update_client_by_id(client_id: int, data: ClientAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.update(clientModel, client_id, data, session)
        return {"status_code": 201, "message": "Updated successfully", "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))
