import os

class LocalApp:
    def create_executable(self, script_name):
        os.system(f"pyinstaller --onefile {script_name}")
        print(f"🖥 {script_name} uygulamaya dönüştürüldü!")

if __name__ == "__main__":
    app = LocalApp()
    app.create_executable("test_script.py")
