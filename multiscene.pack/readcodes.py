# multiscene.pack/readcodes.py

def read_scene_code(file_path):
    """.scene dosyasını okur ve kodu döndürür"""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"{file_path} bulunamadı.")
        return None
