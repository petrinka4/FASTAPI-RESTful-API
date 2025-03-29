from app.repositories.base import BaseRepository
from app.models.card import cardModel

from sqlalchemy.orm import DeclarativeMeta


class CardRepository(BaseRepository):
    Model: DeclarativeMeta = cardModel
