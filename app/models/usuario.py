from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, SmallInteger, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.persona import Persona

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario: Mapped[int] = mapped_column(primary_key=True)
    uuid_usuario: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    username: Mapped[str] = mapped_column(CITEXT, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    rol: Mapped[str] = mapped_column(nullable=False)  # rol_usuario enum

    persona_id: Mapped[Optional[int]] = mapped_column(ForeignKey("persona.id_persona", ondelete="SET NULL"))

    must_change_password: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    persona: Mapped[Optional["Persona"]] = relationship(back_populates="usuario")