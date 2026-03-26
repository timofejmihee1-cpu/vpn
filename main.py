import os
import asyncio
from aiosocks.server import Socks5Server

async def main():
    # Порт от Render
    port = int(os.environ.get("PORT", 8080))
    # Твой пароль из настроек Render
    password = os.environ.get("PROXY_PASSWORD", "happ123")
    
    # Запуск сервера
    server = Socks5Server(host="0.0.0.0", port=port)
    # Добавляем пользователя
    server.add_user("user", password)
    
    print(f"Сервер запущен на порту {port}")
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
