# app/models/refresh_token.py
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID

from sqlalchemy import String, DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.database.database import Base  # ajusta según tu ruta real


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id_refresh_token: Mapped[int] = mapped_column(primary_key=True)
    uuid_refresh_token: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False
    )

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id_usuario", ondelete="CASCADE"),
        nullable=False
    )
    token_hash: Mapped[str] = mapped_column(String, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    revoked_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False
    )

