import capture
import cv2
import time
import os
from overlay import overlay_translations

def cleanup_old_frames():
    """Remove old frame files to save disk space"""
    for file in os.listdir('.'):
        if file.startswith('realtime_frame_') and file.endswith('.png'):
            try:
                os.remove(file)
            except:
                pass

def run_realtime_pipeline(target_fps=5, max_frames=100):
    """
    Run real-time translation pipeline
    
    Args:
        target_fps: Target frames per second (default: 5)
        max_frames: Maximum frames to keep (default: 100)
    """
    print(f"[*] Starting real-time translation pipeline at {target_fps} FPS...")
    print("[*] Press Ctrl+C to stop")
    
    # Clean up old frames
    cleanup_old_frames()
    
    frame_count = 0
    start_time = time.time()
    frame_interval = 1.0 / target_fps
    
    try:
        while True:
            frame_start = time.time()
            
            # Capture screen
            img = capture.capture_screen()
            
            # Process with OCR and translation
            result_img = overlay_translations(img)
            
            # Save frame
            frame_count += 1
            output_path = f"realtime_frame_{frame_count:04d}.png"
            cv2.imwrite(output_path, result_img)
            
            # Calculate timing
            frame_time = time.time() - frame_start
            fps = 1.0 / frame_time if frame_time > 0 else 0
            elapsed_time = time.time() - start_time
            avg_fps = frame_count / elapsed_time if elapsed_time > 0 else 0
            
            print(f"[*] Frame {frame_count:04d} | FPS: {fps:.1f} | Avg: {avg_fps:.1f} | Saved: {output_path}")
            
            # Clean up old frames periodically
            if frame_count % 50 == 0:
                cleanup_old_frames()
            
            # Frame rate control
            sleep_time = max(0, frame_interval - frame_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
            
    except KeyboardInterrupt:
        print(f"\n[*] Stopped after {frame_count} frames")
        print(f"[*] Average FPS: {avg_fps:.1f}")
        print(f"[*] Total runtime: {elapsed_time:.1f} seconds")

if __name__ == "__main__":
    # You can adjust these parameters
    run_realtime_pipeline(target_fps=3, max_frames=50)  # 3 FPS, keep last 50 frames 