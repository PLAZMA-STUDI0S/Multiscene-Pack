import os

class FolderController:
    def __init__(self, path):
        self.path = path

    def create_folder(self):
        os.makedirs(self.path, exist_ok=True)
        print(f"📂 Klasör oluşturuldu: {self.path}")

    def delete_folder(self):
        if os.path.exists(self.path):
            os.rmdir(self.path)
            print(f"🗑 Klasör silindi: {self.path}")
        else:
            print("⚠ Klasör bulunamadı.")

if __name__ == "__main__":
    folder = FolderController("test_folder")
    folder.create_folder()
    folder.delete_folder()
