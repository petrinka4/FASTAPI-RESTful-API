from app.repositories.base import BaseRepository
from app.models.client import clientModel

from sqlalchemy.orm import DeclarativeMeta


class ClientRepository(BaseRepository):
    Model: DeclarativeMeta = clientModel
