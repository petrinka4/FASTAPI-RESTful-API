from typing import List
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

from app.models.base import Base





class accountModel(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"))
    #relationship
    cards=relationship("cardModel",back_populates="account", lazy="selectin")
    bank=relationship("bankModel",back_populates="accounts", lazy="selectin")
    client=relationship("clientModel",back_populates="accounts", lazy="selectin")

