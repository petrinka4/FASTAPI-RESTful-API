from app.repositories.base import BaseRepository
from app.models.account import accountModel

from sqlalchemy.orm import DeclarativeMeta


class AccountRepository(BaseRepository):
    Model: DeclarativeMeta = accountModel