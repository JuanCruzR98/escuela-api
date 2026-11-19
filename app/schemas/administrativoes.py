from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from app.schemas.personaes import PersonaCreate, PersonaResponse


class AdministrativoCreate(BaseModel):
    persona: PersonaCreate
    codigo_administrativo: str = Field(..., min_length=1, max_length=20)
    cargo: str = Field(..., min_length=1, max_length=100)
    tareas: Optional[str] = None


class AdministrativoUpdate(BaseModel):
    codigo_administrativo: Optional[str] = Field(None, min_length=1, max_length=20)
    cargo: Optional[str] = Field(None, min_length=1, max_length=100)
    tareas: Optional[str] = None


class AdministrativoResponse(BaseModel):
    id_administrativo: int
    uuid_administrativo: UUID
    codigo_administrativo: str
    cargo: str
    tareas: Optional[str] = None
    persona: PersonaResponse
    created_at: datetime

    model_config = {"from_attributes": True}