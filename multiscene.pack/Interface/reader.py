# multiscene.pack/Interface/reader.py

def read_file(file_path):
    """Dosyayı okur ve içeriğini döndürür"""
    with open(file_path, 'r') as file:
        return file.read()
