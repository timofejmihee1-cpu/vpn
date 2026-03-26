import os
from pysocks5 import Socks5Server

def main():
    # Порт от Render
    port = int(os.environ.get("PORT", 8080))
    # Твой пароль из настроек Render (или happ123 по умолчанию)
    password = os.environ.get("PROXY_PASSWORD", "happ123")
    
    # Создаем сервер. Пользователь: user, Пароль: password
    server = Socks5Server(
        host="0.0.0.0", 
        port=port, 
        auth={"user": password}
    )
    
    print(f"VPN Server starting on port {port}...")
    server.run()

if __name__ == "__main__":
    main()
