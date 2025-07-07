import cv2
import numpy as np
import easyocr
from translate import translate_text

reader = easyocr.Reader(['en', 'ja'])

def overlay_translations(image):
    # Make a copy of the image to avoid modifying the original
    result_image = image.copy()
    
    results = reader.readtext(image)
    
    boxes = []
    original_texts = []
    
    for bbox, text, _ in results:
        # Convert bbox points to int
        pts = np.array([[int(x), int(y)] for [x, y] in bbox], dtype=np.int32)
        boxes.append(pts)
        original_texts.append(text)

    # Translate original text
    translated_texts = translate_text(original_texts)

    for pts, translated in zip(boxes, translated_texts):
        # Draw black polygon to mask original text
        cv2.fillPoly(result_image, [pts], color=(0, 0, 0))

        # Get top-left corner for putting text
        x, y = pts[0]

        # Draw translated text in white
        cv2.putText(result_image, translated, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2, cv2.LINE_AA)

    return result_image
