from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey
from models.base import Base

class filialModel(Base):
    __tablename__="filials"
    id:Mapped[int]=mapped_column(primary_key=True)
    bank_id:Mapped[int]=mapped_column(ForeignKey("banks.id"))
    city_id:Mapped[int]=mapped_column(ForeignKey("cities.id"))