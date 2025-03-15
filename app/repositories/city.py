from app.repositories.base import BaseRepository
from app.models.city import cityModel

from sqlalchemy.orm import DeclarativeMeta


class CityRepository(BaseRepository):
    Model: DeclarativeMeta = cityModel
