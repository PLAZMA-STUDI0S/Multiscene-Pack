from multiconnect import MultiConnect

class ServerOn:
    def __init__(self, host="localhost", port=12345):
        self.server = MultiConnect(host, port)

    def start_server(self):
        print("🚀 Sunucu başlatılıyor...")
        self.server.connect()

if __name__ == "__main__":
    server = ServerOn()
    server.start_server()
