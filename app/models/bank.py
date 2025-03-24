from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.models.base import Base


class bankModel(Base):
    __tablename__ = "banks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(255))  # Указание длины для VARCHAR
    #relationship
    accounts=relationship("accountModel",back_populates="bank", lazy="selectin")
    branches=relationship("branchModel",back_populates="bank", lazy="selectin")