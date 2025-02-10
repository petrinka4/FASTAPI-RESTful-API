from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import ForeignKey
class Base(DeclarativeBase):
    pass

class accountModel(Base):
    __tablename__="accounts"
    id:Mapped[int]=mapped_column(primary_key=True)
    balance:Mapped[int]
    client_id:Mapped[int]=mapped_column(ForeignKey("clients.id"))
    bank_id:Mapped[int]=mapped_column(ForeignKey("banks.id"))
