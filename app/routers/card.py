from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.card import CardAddSchema
from app.repositories.card import CardRepository

router_card = APIRouter(
    prefix="/cards",
    tags=["card"]
)

# получение всех карт


@router_card.get("", status_code=status.HTTP_200_OK)
async def get_cards(session: AsyncSession = Depends(get_session)):
    cards = await CardRepository.get_all(session)
    return cards

# добавление карты


@router_card.post("", status_code=status.HTTP_201_CREATED)
async def create_card(data: CardAddSchema, session: AsyncSession = Depends(get_session)):
    result = await CardRepository.create(data, session)
    return {"object": result}

# удаление карты по id


@router_card.delete("/{card_id}", status_code=status.HTTP_200_OK)
async def delete_card(card_id: int, session: AsyncSession = Depends(get_session)):
    await CardRepository.delete(card_id,  session)
    return {"message": "Deleted successfully"}

# получение карты по id


@router_card.get("/{card_id}", status_code=status.HTTP_200_OK)
async def get_card_by_id(card_id: int, session: AsyncSession = Depends(get_session)):
    result = await CardRepository.get_one(card_id,  session)
    return result

# апдейт карты по id


@router_card.put("/{card_id}", status_code=status.HTTP_200_OK)
async def update_card_by_id(card_id: int, data: CardAddSchema, session: AsyncSession = Depends(get_session)):
    result = await CardRepository.update(card_id, data, session)
    return {"object": result}
