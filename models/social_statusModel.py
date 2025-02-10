from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass


class social_statusModel(Base):
    __tablename__="social_statuses"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]