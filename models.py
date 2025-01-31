from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import ForeignKey
class Base(DeclarativeBase):
    pass

class bankModel(Base):
    __tablename__="banks"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

class cityModel(Base):
    __tablename__="cities"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

class filialModel(Base):
    __tablename__="filials"
    id:Mapped[int]=mapped_column(primary_key=True)
    bank_id:Mapped[int]=mapped_column(ForeignKey("banks.id"))
    city_id:Mapped[int]=mapped_column(ForeignKey("cities.id"))

class social_statusModel(Base):
    __tablename__="social_statuses"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

class clientModel(Base):
    __tablename__="clients"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    social_status_id:Mapped[int]=mapped_column(ForeignKey("social_statuses.id"))

class accountModel(Base):
    __tablename__="accounts"
    id:Mapped[int]=mapped_column(primary_key=True)
    balance:Mapped[int]
    client_id:Mapped[int]=mapped_column(ForeignKey("clients.id"))
    bank_id:Mapped[int]=mapped_column(ForeignKey("banks.id"))

class cardModel(Base):
    __tablename__="cards"
    id:Mapped[int]=mapped_column(primary_key=True)
    balance:Mapped[int]
    account_id:Mapped[int]=mapped_column(ForeignKey("accounts.id"))