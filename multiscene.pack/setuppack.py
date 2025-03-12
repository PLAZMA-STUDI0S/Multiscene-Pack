# multiscene.pack/setuppack.py

from .folderadder import add_folder
from .readcodes import read_scene_code

def setup_package():
    """Kütüphaneyi başlatma ve gerekli dosyaları hazırlama"""
    print("Kütüphane başlatılıyor...")
    # Yeni bir klasör ekleyelim
    add_folder('new_project_folder')
    # Bir .scene dosyası oku
    code = read_scene_code('project.scene')
    if code:
        print(f"Scene kodu başarıyla okundu:\n{code}")
