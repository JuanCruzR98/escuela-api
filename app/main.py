import uvicorn
from .models.server import Server
server = Server()
app = server.get_app()

if __name__ == "__main__":
    uvicorn.run(app=app, port=3000)