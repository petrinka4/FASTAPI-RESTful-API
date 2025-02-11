from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class cityModel(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
