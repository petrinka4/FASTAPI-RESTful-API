from typing import Annotated
from fastapi import APIRouter, Depends

from models.filialModel import filialModel
from schemas import FilialAddSchema
from operations.filialOp import FilialOperations
from operations.generalOp import GeneralOperations

router_filial=APIRouter(
    prefix="/filials",
    tags=["filial"]
)

#получение всех филиалов
@router_filial.get("")
async def get_filials():
    filials=await GeneralOperations.get_all(filialModel)
    return filials

#добавление филиала
@router_filial.post("")
async def add_filial(data: Annotated[FilialAddSchema, Depends()]):
    result = await FilialOperations.add_one_filial(data)
    if isinstance(result, dict) and "error" in result:
        return {"ok": False, "error": result["error"]}
    return {"ok": True, "id": result}

#удаление филиала по id
@router_filial.delete("/{filial_id}") 
async def delete_filial(filial_id:int):
    data=await GeneralOperations.delete_one(filial_id,filialModel)
    return data

#получение филиала по id
@router_filial.get("/{filial_id}")
async def get_filial_by_id(filial_id:int):
  data=await GeneralOperations.get_one(filial_id,filialModel)
  return data

#апдейт филиала по id
@router_filial.put("/{filial_id}")
async def update_filial_by_id(filial_id:int,data:Annotated[FilialAddSchema,Depends()]):
    result=await FilialOperations.update_filial(filial_id,data)
    return result