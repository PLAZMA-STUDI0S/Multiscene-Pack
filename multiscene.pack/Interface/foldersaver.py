# multiscene.pack/Interface/foldersaver.py

import json

def save_folder_data(folder_name, data):
    """Klasör verilerini JSON formatında kaydeder"""
    with open(f"{folder_name}/data.json", 'w') as f:
        json.dump(data, f)
    print(f"{folder_name} verileri kaydedildi.")
