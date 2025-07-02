# Attempting to build an OCR which can translate text on a specified screen resolution

## Step 1: Capture.py
- using OpenCV to capture current screen of user
- region acts as a way to access capture resolution of screen
- uses main monitor to capture

## Step 2: perform basic OCR
- import the captured screen
- return the texts captured from capture via easyOCR