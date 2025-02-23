from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String

from app.models.base import Base


class clientModel(Base):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    social_status_id: Mapped[int] = mapped_column(
        ForeignKey("social_statuses.id"))
