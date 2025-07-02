import easyocr
from capture import capture_screen

reader = easyocr.Reader(['en', 'ja'])

def ocr_image(image):
    results = reader.readtext(image)
    return [text for text, _, _ in results]

if __name__ == "__main__":
    img = capture_screen()
    texts = ocr_image(img)
    for text in texts:
        print(text)