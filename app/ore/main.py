# Third Party Library
from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "index.jinja2.html", {"request": request}
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"送ったメッセージ: {data}")
