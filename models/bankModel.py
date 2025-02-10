from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass
class bankModel(Base):
    __tablename__="banks"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
