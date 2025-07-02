# capture.py
import mss
import numpy as np
import cv2

def capture_screen(region=None):
    with mss.mss() as sct:
        monitor = region if region else sct.monitors[1]
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        return img[..., :3]

if __name__ == "__main__":
    img = capture_screen()
    cv2.imshow("Screenshot", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
