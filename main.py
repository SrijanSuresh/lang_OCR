import capture
import cv2
from overlay import overlay_translations

def run_pipeline():
    print("[*] Capturing screen...")
    img = capture.capture_screen()

    print("[*] Overlaying translations...")
    result_img = overlay_translations(img)

    # Save result instead of displaying
    output_path = "translated_overlay.png"
    cv2.imwrite(output_path, result_img)
    print(f"[*] Result saved to: {output_path}")

if __name__ == "__main__":
    run_pipeline()