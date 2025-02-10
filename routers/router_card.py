from typing import Annotated
from fastapi import APIRouter, Depends

from models.cardModel import cardModel
from schemas import CardAddSchema
from operations.cardOp import CardOperations
from operations.generalOp import GeneralOperations

router_card=APIRouter(
    prefix="/cards",
    tags=["card"]
)

#получение всех карт
@router_card.get("")
async def get_cards():
    cards=await GeneralOperations.get_all(cardModel)
    return cards

#добавление карты
@router_card.post("")
async def add_card(data: Annotated[CardAddSchema, Depends()]):
    result = await CardOperations.add_one_card(data)
    if isinstance(result, dict) and "error" in result:
        return {"ok": False, "error": result["error"]}
    return {"ok": True, "id": result}

#удаление карты по id
@router_card.delete("/{card_id}") 
async def delete_card(card_id:int):
    data=await GeneralOperations.delete_one(card_id,cardModel)
    return data

#получение карты по id
@router_card.get("/{card_id}")
async def get_card_by_id(card_id:int):
  data=await GeneralOperations.get_one(card_id,cardModel)
  return data

#апдейт карты по id
@router_card.put("/{card_id}")
async def update_card_by_id(card_id:int,data:Annotated[CardAddSchema,Depends()]):
    result=await CardOperations.update_card(card_id,data)
    return result