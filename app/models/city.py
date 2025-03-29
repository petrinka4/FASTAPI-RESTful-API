from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.models.base import Base


class cityModel(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    #relationship
    branches=relationship("branchModel",back_populates="city", lazy="selectin")
