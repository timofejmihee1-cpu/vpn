import os
import uvicorn
import base64
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

# 1. Твой сайт для "анти-спячки" (открой его в браузере на телефоне)
@app.get("/")
async def root():
    return PlainTextResponse("ok")

# 2. Секретный путь, который выдаст конфиг для HAPP
@app.get("/config")
async def get_config():
    # Создаем Shadowsocks ссылку (формат, который понимают V2Ray клиенты)
    # Метод: aes-256-gcm, Пароль: happ777
    server_address = "vpn-u0c2.onrender.com"
    user_pass = base64.b64encode(b"aes-256-gcm:happ777").decode('utf-8')
    ss_link = f"ss://{user_pass}@{server_address}:443#MyRenderVPN"
    
    # Возвращаем это как текст, который HAPP сможет импортировать
    return PlainTextResponse(ss_link)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
