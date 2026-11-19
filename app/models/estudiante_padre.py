from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
   from app.models.estudiante import Estudiante
   from app.models.padre import Padre

class EstudiantePadre(Base):
    __tablename__ = "estudiante_padre"

    id_estudiante_padre: Mapped[int] = mapped_column(primary_key=True)
    uuid_estudiante_padre: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id_estudiante", ondelete="CASCADE"), nullable=False)
    padre_id: Mapped[int] = mapped_column(ForeignKey("padres.id_padre", ondelete="CASCADE"), nullable=False)

    parentesco: Mapped[str] = mapped_column(String(30), nullable=False)
    es_responsable_principal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    estudiante: Mapped["Estudiante"] = relationship(back_populates="padres_rel")
    padre: Mapped["Padre"] = relationship(back_populates="estudiantes_rel")

    __table_args__ = (
        UniqueConstraint("estudiante_id", "padre_id", name="estudiante_padre_estudiante_id_padre_id_key"),
    )