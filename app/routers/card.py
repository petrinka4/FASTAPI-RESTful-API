from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.card import cardModel
from app.schemas.card import CardAddSchema
from app.resources.general import GeneralResources

router_card = APIRouter(
    prefix="/cards",
    tags=["card"]
)

# получение всех карт


@router_card.get("")
async def get_cards(session: AsyncSession = Depends(get_session)):
    try:
        cards = await GeneralResources.get_all(cardModel, session)
        return cards
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# добавление карты


@router_card.post("")
async def create_card(data: CardAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.create(cardModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# удаление карты по id


@router_card.delete("/{card_id}")
async def delete_card(card_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete(card_id, cardModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# получение карты по id


@router_card.get("/{card_id}")
async def get_card_by_id(card_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(card_id, cardModel, session)
        return result
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# апдейт карты по id


@router_card.put("/{card_id}")
async def update_card_by_id(card_id: int, data: CardAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.update(cardModel, card_id, data, session)
        return {"status_code": 201, "message": "Updated successfully", "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))
