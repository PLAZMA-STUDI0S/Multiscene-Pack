# multiscene.pack/Interface/require.py

import subprocess

def install_requirements():
    """Gerekli bağımlılıkları yükler"""
    requirements = ['requests', 'numpy']
    for package in requirements:
        subprocess.run([f"pip install {package}"])
    print("Bağımlılıklar yüklendi.")
