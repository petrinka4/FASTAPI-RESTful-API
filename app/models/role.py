from app.models.base import Base

from sqlalchemy import Boolean, ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column,relationship


class roleModel(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(255))
    #relationship
    users=relationship("userModel",back_populates="role", lazy="selectin")
    


