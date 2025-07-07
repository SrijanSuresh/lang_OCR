from flask import Flask, render_template, Response, jsonify, request
import cv2
import base64
import threading
import time
import io
from PIL import Image
import numpy as np
import mss
from capture import capture_screen
from overlay import overlay_translations

app = Flask(__name__)

# Global variables for real-time processing
current_frame = None
current_translations = []
is_capturing = False
capture_thread = None
selected_monitor = 1
custom_resolution = None
show_border = True

def get_available_monitors():
    """Get list of available monitors"""
    with mss.mss() as sct:
        return [
            {
                'id': i,
                'width': monitor['width'],
                'height': monitor['height'],
                'left': monitor['left'],
                'top': monitor['top']
            }
            for i, monitor in enumerate(sct.monitors[1:], 1)  # Skip monitor 0 (all monitors combined)
        ]

def capture_screen_with_options(monitor_id=1, custom_region=None):
    """Capture screen with specific monitor and region options"""
    with mss.mss() as sct:
        if custom_region:
            # Use custom region
            monitor = custom_region
        else:
            # Use selected monitor
            monitor = sct.monitors[monitor_id]
        
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        # Convert BGRA to BGR (OpenCV format)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

def add_border_to_image(image, border_color=(0, 0, 255), border_width=5):
    """Add a colored border around the image"""
    height, width = image.shape[:2]
    # Draw border rectangle
    cv2.rectangle(image, (0, 0), (width-1, height-1), border_color, border_width)
    return image

def capture_loop():
    """Background thread for continuous screen capture and processing"""
    global current_frame, current_translations, is_capturing, selected_monitor, custom_resolution, show_border
    
    while is_capturing:
        try:
            # Capture screen with selected options
            img = capture_screen_with_options(selected_monitor, custom_resolution)
            
            # Add border if enabled
            if show_border:
                img = add_border_to_image(img)
            
            # Process with OCR and translation
            result_img = overlay_translations(img)
            
            # Convert to base64 for web display
            _, buffer = cv2.imencode('.jpg', result_img, [cv2.IMWRITE_JPEG_QUALITY, 80])
            img_base64 = base64.b64encode(buffer).decode('utf-8')
            
            current_frame = img_base64
            
            time.sleep(0.1)  # 10 FPS
            
        except Exception as e:
            print(f"Error in capture loop: {e}")
            time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_monitors')
def get_monitors():
    """Get available monitors"""
    monitors = get_available_monitors()
    return jsonify({"monitors": monitors})

@app.route('/set_monitor', methods=['POST'])
def set_monitor():
    """Set the monitor to capture"""
    global selected_monitor, custom_resolution
    data = request.get_json()
    
    if 'monitor_id' in data:
        selected_monitor = int(data['monitor_id'])
        custom_resolution = None  # Reset custom resolution
        return jsonify({"status": "success", "message": f"Monitor {selected_monitor} selected"})
    
    return jsonify({"status": "error", "message": "Invalid monitor ID"})

@app.route('/set_custom_resolution', methods=['POST'])
def set_custom_resolution():
    """Set custom resolution/region"""
    global custom_resolution
    data = request.get_json()
    
    try:
        custom_resolution = {
            'left': int(data['left']),
            'top': int(data['top']),
            'width': int(data['width']),
            'height': int(data['height'])
        }
        return jsonify({"status": "success", "message": "Custom resolution set"})
    except:
        return jsonify({"status": "error", "message": "Invalid resolution parameters"})

@app.route('/toggle_border', methods=['POST'])
def toggle_border():
    """Toggle the red border around the capture area"""
    global show_border
    show_border = not show_border
    return jsonify({"status": "success", "border_enabled": show_border})

@app.route('/start_capture')
def start_capture():
    global is_capturing, capture_thread
    
    if not is_capturing:
        is_capturing = True
        capture_thread = threading.Thread(target=capture_loop, daemon=True)
        capture_thread.start()
        return jsonify({"status": "started"})
    return jsonify({"status": "already_running"})

@app.route('/stop_capture')
def stop_capture():
    global is_capturing
    is_capturing = False
    return jsonify({"status": "stopped"})

@app.route('/get_frame')
def get_frame():
    global current_frame
    if current_frame:
        return jsonify({"frame": current_frame})
    return jsonify({"frame": None})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 