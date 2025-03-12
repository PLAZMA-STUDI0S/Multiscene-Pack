import socket

class MultiConnect:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Bağlantı başarılı: {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"Bağlantı hatası: {e}")
            return False

    def disconnect(self):
        if self.socket:
            self.socket.close()
            print("Bağlantı kapatıldı.")
        else:
            print("Henüz bir bağlantı yok.")

if __name__ == "__main__":
    connection = MultiConnect()
    if connection.connect():
        connection.disconnect()

