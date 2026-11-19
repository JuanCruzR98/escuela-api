from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import auth

class Server:
    def __init__(self):
        self.app = FastAPI()
        self.__middlewares()
        self.__routes()

    def get_app(self):
        return self.app
    
    def __middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,allow_origins=["http://localhost:8001","http://127.0.0.1:8001"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"]
        )
    
    def __routes(self):
        
       @self.app.exception_handler(404)
       async def not_found(request, exc):
           if(request.url.path.startswith("/api")):
               return JSONResponse({"msg":"Endpoint not found in {request.url.path}"},status_code=404)
             
       self.app.include_router(auth.router,prefix="/api") 
    