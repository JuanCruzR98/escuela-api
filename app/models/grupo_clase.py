from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, SmallInteger, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.anio_academico import AnioAcademico
    from app.models.grado import Grado
    from app.models.matricula import Matricula

class GrupoClase(Base):
    __tablename__ = "grupos_clase"

    id_grupo: Mapped[int] = mapped_column(primary_key=True)
    uuid_grupo: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    anio_id: Mapped[int] = mapped_column(ForeignKey("anios_academicos.id_anio", ondelete="RESTRICT"), nullable=False)
    grado_id: Mapped[int] = mapped_column(ForeignKey("grados.id_grado", ondelete="RESTRICT"), nullable=False)

    nombre: Mapped[str] = mapped_column(String(20), nullable=False)
    turno: Mapped[str] = mapped_column(nullable=False)  # turno_grupo enum
    cupo_maximo: Mapped[Optional[int]] = mapped_column(SmallInteger, default=30)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    anio: Mapped["AnioAcademico"] = relationship(back_populates="grupos")
    grado: Mapped["Grado"] = relationship(back_populates="grupos")
    matriculas: Mapped[List["Matricula"]] = relationship(back_populates="grupo")

    __table_args__ = (
        UniqueConstraint("anio_id", "grado_id", "nombre", name="grupos_clase_anio_id_grado_id_nombre_key"),
        CheckConstraint("cupo_maximo IS NULL OR cupo_maximo > 0", name="grupos_clase_cupo_maximo_check"),
    )