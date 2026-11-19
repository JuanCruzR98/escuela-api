from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.persona import Persona
    from app.models.docente_especialidad import DocenteEspecialidad
    


class Docente(Base):
    __tablename__ = "docentes"

    id_docente: Mapped[int] = mapped_column(primary_key=True)
    uuid_docente: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    persona_id: Mapped[int] = mapped_column(ForeignKey("persona.id_persona", ondelete="CASCADE"), unique=True, nullable=False)
    codigo_docente: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    persona: Mapped["Persona"] = relationship(back_populates="docente")
    especialidades_rel: Mapped[List["DocenteEspecialidad"]] = relationship(back_populates="docente")