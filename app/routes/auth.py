from datetime import timedelta
import json
import jwt
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import get_db
from app.schemas import TokenResponse,UsuarioLogin
from app.controllers.auth_controller import AuthController

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/login", response_model=TokenResponse)
async def login(
    data: UsuarioLogin,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
          return await AuthController.login(
            data,
            response,
            db) 
    
@router.post("/forgot-password")
async def forgot_password():


@router.post("/recover")
async def restore_password():
    return JSONResponse({"msg":"Hola desde restores mi objetivo es restablecer la contraseña"},status_code=status.HTTP_201_CREATED)

@router.post("/logout")
async def logout():
    return JSONResponse({"msg":"Hola desde logout"},status_code=status.HTTP_200_OK)

@router.post("/refresh")
async def refresh():
    return JSONResponse({"msg":"Hola desde refresh mi objetivo es refrescar el token"},status_code=status.HTTP_200_OK)
