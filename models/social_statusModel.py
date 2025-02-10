from sqlalchemy.orm import Mapped,mapped_column

from models.base import Base


class social_statusModel(Base):
    __tablename__="social_statuses"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]