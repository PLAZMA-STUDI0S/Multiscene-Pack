class FPSConnecter:
    def __init__(self, fps=60):
        self.fps = fps

    def set_fps(self, new_fps):
        self.fps = new_fps
        print(f"🔧 FPS ayarlandı: {self.fps}")

    def get_fps(self):
        return self.fps

if __name__ == "__main__":
    fps_manager = FPSConnecter()
    print(f"Mevcut FPS: {fps_manager.get_fps()}")
    fps_manager.set_fps(120)
