from typing import Annotated
from fastapi import APIRouter, Depends

from models.clientModel import clientModel
from schemas import ClientAddSchema
from operations.clientOp import ClientOperations
from operations.generalOp import GeneralOperations

router_client=APIRouter(
    prefix="/clients",
    tags=["client"]
)

#получение всех клиентов
@router_client.get("")
async def get_clients():
    clients=await GeneralOperations.get_all(clientModel)
    return clients

#добавление клиента
@router_client.post("")
async def add_client(data: Annotated[ClientAddSchema, Depends()]):
    result = await ClientOperations.add_one_client(data)
    if isinstance(result, dict) and "error" in result:
        return {"ok": False, "error": result["error"]}
    return {"ok": True, "id": result}

#удаление клиента
@router_client.delete("/{client_id}")
async def delete_client(client_id:int):
    result=await GeneralOperations.delete_one(client_id,clientModel)
    return result

#получение клиента по id
@router_client.get("/{client_id}")
async def get_client_by_id(client_id:int):
    result=await GeneralOperations.get_one(client_id,clientModel)
    return result

#апдейт клиента по id
@router_client.put("/{client_id}")
async def update_client_by_id(client_id:int,client:Annotated[ClientAddSchema,Depends()]):
    result=await ClientOperations.update_client(client_id,client)
    return result





