import mss, cv2, numpy as np
import easyocr

reader = easyocr.Reader(['ja'], gpu=True)  # Set gpu=True if supported

with mss.mss() as sct:
    monitor = sct.monitors[1]
    while True:
        img = np.array(sct.grab(monitor))
        result = reader.readtext(img)
        if result:
            text = " ".join([r[1] for r in result])
            print(f"[JP]: {text}")
        if cv2.waitKey(1000) == ord('q'):
            break
