import capture
from ocr import ocr_image
from translate import translate_text

def run_pipeline():
    print("[*] Capturing screen...")
    img = capture.capture_screen()
    
    print("[*] Running OCR...")
    texts = ocr_image(img)
    print(f"[+] Detected: {texts}")
    
    if texts:
        print("[*] Translating...")
        translated = translate_text(texts)
        for orig, trans in zip(texts, translated):
            print(f"{orig} -> {trans}")
    else:
        print("[-] No text detected.")

if __name__ == "__main__":
    run_pipeline()
