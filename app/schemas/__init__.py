from app.schemas.personaes import PersonaCreate, PersonaUpdate, PersonaResponse
from app.schemas.usuarioes import (
    UsuarioCreate, UsuarioUpdate, UsuarioLogin, 
    UsuarioResponse, TokenResponse
)
from app.schemas.estudiantees import EstudianteCreate, EstudianteUpdate, EstudianteResponse
from app.schemas.docentees import DocenteCreate, DocenteUpdate, DocenteResponse
from app.schemas.padrees import PadreCreate, PadreResponse
from app.schemas.administrativoes import (
    AdministrativoCreate, AdministrativoUpdate, AdministrativoResponse
)
from app.schemas.contactoes import (
    TelefonoCreate, TelefonoResponse,
    CorreoCreate, CorreoResponse,
    DireccionCreate, DireccionResponse
)