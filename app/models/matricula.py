from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, SmallInteger, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.grupo_clase import GrupoClase
    from app.models.anio_academico import AnioAcademico
    from app.models.estudiante import Estudiante

class Matricula(Base):
    __tablename__ = "matriculas"

    id_matricula: Mapped[int] = mapped_column(primary_key=True)
    uuid_matricula: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id_estudiante", ondelete="RESTRICT"), nullable=False)
    anio_id: Mapped[int] = mapped_column(ForeignKey("anios_academicos.id_anio", ondelete="RESTRICT"), nullable=False)
    grupo_id: Mapped[int] = mapped_column(ForeignKey("grupos_clase.id_grupo", ondelete="RESTRICT"), nullable=False)

    fecha_matricula: Mapped[date] = mapped_column(Date, server_default=text("CURRENT_DATE"), nullable=False)
    estado: Mapped[str] = mapped_column(String(20), default="activa", nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    estudiante: Mapped["Estudiante"] = relationship(back_populates="matriculas")
    anio: Mapped["AnioAcademico"] = relationship(back_populates="matriculas")
    grupo: Mapped["GrupoClase"] = relationship(back_populates="matriculas")

    __table_args__ = (
        UniqueConstraint("estudiante_id", "anio_id", name="matriculas_estudiante_id_anio_id_key"),
        CheckConstraint(
            "estado IN ('activa', 'retirada', 'trasladada', 'finalizada')",
            name="matriculas_estado_check"
        ),
    )