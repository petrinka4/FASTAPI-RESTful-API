from sqlalchemy.orm import Mapped,mapped_column
from models.base import Base

class bankModel(Base):
    __tablename__="banks"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
