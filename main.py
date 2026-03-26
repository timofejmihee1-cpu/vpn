import os
import asyncio
from aiosocksrv.server import SocksServer

async def main():
    # Render сам назначит порт через эту переменную
    port = int(os.environ.get("PORT", 8080))
    # Твой секретный пароль, который ты укажешь в настройках Render
    password = os.environ.get("PROXY_PASSWORD", "default_pass")
    
    server = SocksServer(host="0.0.0.0", port=port, auth_user="user", auth_pass=password)
    print(f"Сервер запущен на порту {port} с паролем безопасности.")
    
    await server.run_server()

if __name__ == "__main__":
    asyncio.run(main())
