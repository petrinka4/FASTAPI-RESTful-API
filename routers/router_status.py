from typing import Annotated
from fastapi import APIRouter, Depends

from models.social_statusModel import social_statusModel
from schemas import Social_StatusAddSchema
from operations.social_statusOp import StatusOperations
from operations.generalOp import GeneralOperations

router_status=APIRouter(
    prefix="/social_status",
    tags=["status"]
)

#добавление статуса
@router_status.post("")
async def add_status(data:Annotated[Social_StatusAddSchema,Depends()]):
    status_id=await StatusOperations.add_one_status(data)
    return {"ok":True,"id":status_id}


  


#получение всех статусов
@router_status.get("")
async def get_statuses():
    statuses=await GeneralOperations.get_all(social_statusModel)
    return statuses




#удаление статуса по id
@router_status.delete("/{status_id}") 
async def delete_status(status_id:int):
    data=await GeneralOperations.delete_one(status_id,social_statusModel)
    return data
      

#получение статуса по id
@router_status.get("/{status_id}")
async def get_status_by_id(status_id:int):
  data=await GeneralOperations.get_one(status_id,social_statusModel)
  return data

#апдейт статуса по id
@router_status.put("/{status_id}")
async def update_status_by_id(status_id:int,data:Annotated[Social_StatusAddSchema,Depends()]):
    result=await StatusOperations.update_status(status_id,data)
    return result

