import subprocess

class PythonLoad:
    def run_script(self, script_name):
        print(f"▶ {script_name} çalıştırılıyor...")
        subprocess.run(["python", script_name])

if __name__ == "__main__":
    loader = PythonLoad()
    loader.run_script("test_script.py")
