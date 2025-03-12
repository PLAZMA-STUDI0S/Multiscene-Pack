class CodeExtender:
    def __init__(self, code):
        self.code = code

    def fix_code(self):
        corrected_code = self.code.replace("==", "=").replace(";", "")
        print(f"🛠 Düzeltilmiş kod: \n{corrected_code}")

if __name__ == "__main__":
    raw_code = "if x == 10; print('Hata var!');"
    fixer = CodeExtender(raw_code)
    fixer.fix_code()

