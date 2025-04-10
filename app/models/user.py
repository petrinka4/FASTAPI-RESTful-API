from app.models.base import Base

from sqlalchemy import Boolean, ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.models.role import roleModel



class userModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[bytes] = mapped_column(LargeBinary(), nullable=False)  
    role_id: Mapped[int] = mapped_column(ForeignKey(roleModel.id))
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    
    # relationships
    role = relationship("roleModel", back_populates="users", lazy="selectin")
    
    def __init__(self, **kwargs):
        # Хешируем пароль при создании объекта
        from app.auth import utils
        if 'password' in kwargs:
            kwargs['password'] = utils.hash_password(kwargs['password'])
        super().__init__(**kwargs)


    