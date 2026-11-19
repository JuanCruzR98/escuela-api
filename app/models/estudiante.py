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
    from app.models.estudiante_padre import EstudiantePadre
    from app.models.matricula import Matricula
    

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante: Mapped[int] = mapped_column(primary_key=True)
    uuid_estudiante: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    persona_id: Mapped[int] = mapped_column(ForeignKey("persona.id_persona", ondelete="CASCADE"), unique=True, nullable=False)
    escuela_procedencia: Mapped[Optional[int]] = mapped_column(ForeignKey("escuelas.id_escuela", ondelete="SET NULL"))
    matricula: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    persona: Mapped["Persona"] = relationship(back_populates="estudiante")
    padres_rel: Mapped[List["EstudiantePadre"]] = relationship(back_populates="estudiante")
    matriculas: Mapped[List["Matricula"]] = relationship(back_populates="estudiante")