from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.card import cardModel
from app.schemas import CardAddSchema
from app.operations.card import CardOperations
from app.operations.general import GeneralOperations

router_card = APIRouter(
    prefix="/cards",
    tags=["card"]
)

# получение всех карт


@router_card.get("")
async def get_cards(session: AsyncSession = Depends(get_session)):
    cards = await GeneralOperations.get_all(cardModel, session)
    return cards

# добавление карты


@router_card.post("")
async def add_card(data: CardAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await CardOperations.add_card(cardModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# удаление карты по id


@router_card.delete("/{card_id}")
async def delete_card(card_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralOperations.delete_one(card_id, cardModel,session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# получение карты по id


@router_card.get("/{card_id}")
async def get_card_by_id(card_id: int):
    data = await GeneralOperations.get_one(card_id, cardModel)
    return data

# апдейт карты по id


@router_card.put("/{card_id}")
async def update_card_by_id(card_id: int, data: Annotated[CardAddSchema, Depends()]):
    result = await CardOperations.update_card(card_id, data)
    return result
