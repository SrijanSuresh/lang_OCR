# capture.py
import mss
import numpy as np
import cv2

def capture_screen(region=None):
    with mss.mss() as sct:
        monitor = region if region else sct.monitors[1]
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        # Convert BGRA to BGR (OpenCV format)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

if __name__ == "__main__":
    img = capture_screen()
    # Save screenshot instead of displaying
    cv2.imwrite("screenshot.png", img)
    print("[*] Screenshot saved to: screenshot.png")
