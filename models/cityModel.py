from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class cityModel(Base):
    __tablename__="cities"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]