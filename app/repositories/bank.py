from app.repositories.base import BaseRepository
from app.models.bank import bankModel

from sqlalchemy.orm import DeclarativeMeta


class BankRepository(BaseRepository):
    Model: DeclarativeMeta = bankModel
