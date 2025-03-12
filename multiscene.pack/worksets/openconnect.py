from multiconnect import MultiConnect

class OpenConnect:
    def __init__(self, connection):
        self.connection = connection

    def check_connection(self):
        if self.connection.socket:
            print("Bağlantı aktif.")
            return True
        else:
            print("Bağlantı yok.")
            return False

if __name__ == "__main__":
    connection = MultiConnect()
    if connection.connect():
        open_connection = OpenConnect(connection)
        open_connection.check_connection()
        connection.disconnect()
