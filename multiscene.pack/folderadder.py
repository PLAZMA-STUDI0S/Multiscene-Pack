# multiscene.pack/folderadder.py

import os

def add_folder(folder_name):
    """Yeni bir klasör ekler"""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"{folder_name} klasörü başarıyla oluşturuldu.")
    else:
        print(f"{folder_name} klasörü zaten var.")
