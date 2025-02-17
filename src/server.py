from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from starlette.websockets import WebSocketDisconnect
from motor_control import move_robot, set_motor_speed
from text_to_speech import speak_text
from video_stream import gen_frames

app = FastAPI()

# Allow all origins (adjust for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            if data in ['+', '-']:
                set_motor_speed(data)
            else:
                move_robot(data)
            await websocket.send_text(f"Action: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

@app.post("/speak")
async def speak(request: Request):
    form_data = await request.form()
    text = form_data['text']
    return speak_text(text)

@app.get("/")
async def get():
    with open("templates/control_panel.html", "r") as file:
        return HTMLResponse(file.read())

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    try:
        uvicorn.run(app, host='0.0.0.0', port=8000)
    except KeyboardInterrupt:
        pass
