from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from app.schemas.personaes import PersonaCreate, PersonaResponse


class EstudianteCreate(BaseModel):
    persona: PersonaCreate
    matricula: str = Field(..., min_length=1, max_length=20)
    escuela_procedencia: Optional[int] = None


class EstudianteUpdate(BaseModel):
    matricula: Optional[str] = Field(None, min_length=1, max_length=20)
    escuela_procedencia: Optional[int] = None


class EstudianteResponse(BaseModel):
    id_estudiante: int
    uuid_estudiante: UUID
    matricula: str
    escuela_procedencia: Optional[int] = None
    persona: PersonaResponse
    created_at: datetime

    model_config = {"from_attributes": True}