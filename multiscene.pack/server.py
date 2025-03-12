import socket

def start_server():
    host = 'localhost'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server çalışıyor, {host}:{port} adresinde dinleniyor...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Bağlantı kabul edildi: {client_address}")
        client_socket.send(b"Bağlantı başarılı!")  # Bağlantıya mesaj gönder
        client_socket.close()  # Bağlantıyı kes

if __name__ == "__main__":
    start_server()
