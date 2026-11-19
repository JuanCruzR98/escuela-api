from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from app.schemas.personaes import PersonaCreate, PersonaResponse


class DocenteCreate(BaseModel):
    persona: PersonaCreate
    codigo_docente: str = Field(..., min_length=1, max_length=20)


class DocenteUpdate(BaseModel):
    codigo_docente: Optional[str] = Field(None, min_length=1, max_length=20)


class DocenteResponse(BaseModel):
    id_docente: int
    uuid_docente: UUID
    codigo_docente: str
    persona: PersonaResponse
    created_at: datetime

    model_config = {"from_attributes": True}