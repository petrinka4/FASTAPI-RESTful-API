from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import ForeignKey
class Base(DeclarativeBase):
    pass


class cardModel(Base):
    __tablename__="cards"
    id:Mapped[int]=mapped_column(primary_key=True)
    balance:Mapped[int]
    account_id:Mapped[int]=mapped_column(ForeignKey("accounts.id"))