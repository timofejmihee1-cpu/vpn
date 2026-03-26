import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Тот самый адрес для "оживления" сервера
@app.get("/")
async def root():
    return PlainTextResponse("ok")

# Дополнительный путь для проверки
@app.get("/status")
async def status():
    return {"message": "VPN is running"}

if __name__ == "__main__":
    # Render сам назначит порт
    port = int(os.environ.get("PORT", 8080))
    # Запуск веб-сервера
    uvicorn.run(app, host="0.0.0.0", port=port)
