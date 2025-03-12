import time
from openconnect import OpenConnect
from multiconnect import MultiConnect

class ServerRefresh:
    def __init__(self, connection):
        self.connection = OpenConnect(connection)

    def refresh(self):
        while True:
            print("🔄 Sunucu yenileniyor...")
            time.sleep(1)
            if not self.connection.check_connection():
                print("⚠ Bağlantı kayboldu! Sunucu durduruluyor...")
                break

if __name__ == "__main__":
    connection = MultiConnect()
    if connection.connect():
        server_refresh = ServerRefresh(connection)
        server_refresh.refresh()
