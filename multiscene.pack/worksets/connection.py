import socket

class Connection:
    def check_wifi(self):
        try:
            socket.create_connection(("8.8.8.8", 53))
            print("✅ İnternet bağlantısı var!")
            return True
        except OSError:
            print("❌ İnternet bağlantısı yok!")
            return False

if __name__ == "__main__":
    conn = Connection()
    conn.check_wifi()
