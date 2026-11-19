from datetime import datetime, timedelta, timezone

from fastapi import (
    HTTPException,
    Response,
    status
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.models.refresh_token import RefreshToken

from app.repositories.usuario_repository import UsuarioRepository
from app.repositories.refresh_token_repository import (
    RefreshTokenRepository
)

from app.core import (
    verify_password,
    create_access_token,
    create_refresh_token,
    hash_token,
    get_password_hash
)


class AuthService:

    @staticmethod
    async def login(
        data,
        response: Response,
        db: AsyncSession
    ):

        user = await UsuarioRepository.get_login_user(
            db,
            data.username
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario o contraseña incorrectos"
            )

        if not verify_password(
            data.password,
            user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario o contraseña incorrectos"
            )

        access_token = create_access_token(
            {
                "sub": str(user.id_usuario),
                "rol": user.rol,
                "username": user.username,
            }
        )

        refresh_token = create_refresh_token()

        token_hash = hash_token(
            refresh_token
        )

        expires_at = (
            datetime.now(timezone.utc)
            + timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS
            )
        )

        db_refresh = RefreshToken(
            usuario_id=user.id_usuario,
            token_hash=token_hash,
            expires_at=expires_at,
        )

        await RefreshTokenRepository.create(
            db,
            db_refresh
        )

                
        response.set_cookie(
            key=settings.COOKIE_NAME,
            value=refresh_token,
            httponly=True,
            secure=settings.COOKIE_SECURE,
            samesite=settings.COOKIE_SAMESITE,
            max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 86400,
            path="/auth/refresh",
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "rol": user.rol,
            "must_change_password": user.must_change_password,
        }