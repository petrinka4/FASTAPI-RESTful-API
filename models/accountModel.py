from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey
from models.base import Base

class accountModel(Base):
    __tablename__="accounts"
    id:Mapped[int]=mapped_column(primary_key=True)
    balance:Mapped[int]
    client_id:Mapped[int]=mapped_column(ForeignKey("clients.id"))
    bank_id:Mapped[int]=mapped_column(ForeignKey("banks.id"))
