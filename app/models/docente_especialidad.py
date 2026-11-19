from __future__ import annotations

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.municipio import Municipio
    from app.models.docente import Docente
    from app.models.especialidad import Especialidad


class DocenteEspecialidad(Base):
    __tablename__ = "docente_especialidad"

    id_docente_especialidad: Mapped[int] = mapped_column(primary_key=True)
    uuid_docente_especialidad: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    docente_id: Mapped[int] = mapped_column(ForeignKey("docentes.id_docente", ondelete="CASCADE"), nullable=False)
    especialidad_id: Mapped[int] = mapped_column(ForeignKey("especialidades.id_especialidad", ondelete="RESTRICT"), nullable=False)

    es_principal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    docente: Mapped["Docente"] = relationship(back_populates="especialidades_rel")
    especialidad: Mapped["Especialidad"] = relationship(back_populates="docentes_rel")

    __table_args__ = (
        UniqueConstraint("docente_id", "especialidad_id", name="docente_especialidad_docente_id_especialidad_id_key"),
    )
