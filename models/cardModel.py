from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey
from models.base import Base


class cardModel(Base):
    __tablename__="cards"
    id:Mapped[int]=mapped_column(primary_key=True)
    balance:Mapped[int]
    account_id:Mapped[int]=mapped_column(ForeignKey("accounts.id"))