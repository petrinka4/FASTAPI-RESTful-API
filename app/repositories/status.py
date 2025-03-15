from app.repositories.base import BaseRepository
from app.models.social_status import social_statusModel

from sqlalchemy.orm import DeclarativeMeta


class StatusRepository(BaseRepository):
    Model: DeclarativeMeta = social_statusModel
