from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

from app.models.base import Base


class branchModel(Base):
    __tablename__ = "branches"
    id: Mapped[int] = mapped_column(primary_key=True)
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"))
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    #relationship
    bank=relationship("bankModel",back_populates="branches", lazy="selectin")
    city=relationship("cityModel",back_populates="branches", lazy="selectin")
