# Standard Library
from typing import List

# Third Party Library
from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)


app = FastAPI()
# 静的ファイルのパスを指定する
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")
manager = ConnectionManager()


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "index.jinja2.html", {"request": request}
    )


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "index.jinja2.html", {"request": request}
    )


# WebSocketエンドポイント
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"送ったメッセージ: {data}")

    finally:
        await manager.disconnect(websocket)
