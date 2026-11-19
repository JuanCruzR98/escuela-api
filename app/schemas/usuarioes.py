from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class UsuarioCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)
    rol: str = Field(..., pattern="^(estudiante|docente|padre|administrativo|admin_app)$")
    persona_id: Optional[int] = None


class UsuarioUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    rol: Optional[str] = Field(None, pattern="^(estudiante|docente|padre|administrativo|admin_app)$")
    estado: Optional[bool] = None
    must_change_password: Optional[bool] = None


class UsuarioLogin(BaseModel):
    username: str
    password: str
    
    
class UsuarioForgotPassword(BaseModel):
    username: str
    email: EmailStr


class UsuarioResponse(BaseModel):
    id_usuario: int
    uuid_usuario: UUID
    username: str
    rol: str
    persona_id: Optional[int] = None
    must_change_password: bool
    estado: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    rol: str
    must_change_password: bool