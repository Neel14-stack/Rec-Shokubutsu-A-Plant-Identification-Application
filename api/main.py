from fastapi import FastAPI,File, UploadFile
from io import BytesIO
from PIL import Image
import tensorflow as tf
import uvicorn
import socket
socket.getaddrinfo('127.0.0.1', 8080)

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello I'm alive server"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)

)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1',port = 8080)