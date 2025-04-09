from app.models.user import userModel
from app.repositories.base import BaseRepository

from sqlalchemy.orm import DeclarativeMeta


class UserRepository(BaseRepository):
    Model: DeclarativeMeta = userModel
