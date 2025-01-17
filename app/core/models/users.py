from pydantic import EmailStr
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db.connector import Base
from app.core.models.mixins import CreatedAtUpdatedAtMixin, UUIDMixin


class User(Base, UUIDMixin, CreatedAtUpdatedAtMixin):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[EmailStr] = mapped_column(String, index=True, unique=True)
    password: Mapped[str] = mapped_column(String(255))

    # admin section
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
