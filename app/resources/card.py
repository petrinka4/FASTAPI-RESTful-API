from fastapi import HTTPException

from app.resources.general import GeneralResources
from app.validation.card import validateCard
from app.validation.general import ValidateServise
from app.models.card import cardModel

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class CardResources:

    @classmethod
    async def add_card(cls, data: BaseModel, session: AsyncSession):
        if (await validateCard(data, session)):
            return await GeneralResources.add_one(cardModel, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")

    @classmethod
    async def update_card(cls,  card_id: int, data, session):
        if (await validateCard(data, session) and await ValidateServise.validate_id_existence(cardModel, "id", card_id, session)):
            return await GeneralResources.update_one(cardModel, card_id, data, session)
        raise HTTPException(status_code=400, detail=f"Incorrect data")
