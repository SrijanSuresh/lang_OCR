import capture
import cv2
import time
from overlay import overlay_translations

def run_realtime_pipeline():
    print("[*] Starting real-time translation pipeline...")
    print("[*] Press Ctrl+C to stop")
    
    frame_count = 0
    start_time = time.time()
    
    try:
        while True:
            frame_start = time.time()
            
            # Capture screen
            img = capture.capture_screen()
            
            # Process with OCR and translation
            result_img = overlay_translations(img)
            
            # Save frame with timestamp
            frame_count += 1
            output_path = f"realtime_frame_{frame_count:04d}.png"
            cv2.imwrite(output_path, result_img)
            
            # Calculate and display FPS
            frame_time = time.time() - frame_start
            fps = 1.0 / frame_time if frame_time > 0 else 0
            
            elapsed_time = time.time() - start_time
            avg_fps = frame_count / elapsed_time if elapsed_time > 0 else 0
            
            print(f"[*] Frame {frame_count:04d} | Current FPS: {fps:.1f} | Avg FPS: {avg_fps:.1f} | Saved: {output_path}")
            
            # Optional: Add a small delay to control frame rate
            # time.sleep(0.1)  # 10 FPS max
            
    except KeyboardInterrupt:
        print(f"\n[*] Stopped after {frame_count} frames")
        print(f"[*] Average FPS: {avg_fps:.1f}")

if __name__ == "__main__":
    run_realtime_pipeline()