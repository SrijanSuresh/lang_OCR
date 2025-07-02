# Attempting to build an OCR which can translate text on a specified screen resolution

## Step 1: Capture.py
- using OpenCV to capture current screen of user
- region acts as a way to access capture resolution of screen
- uses main monitor to capture

## Step 2: Perform basic OCR
- import the captured screen
- return the texts captured from capture via easyOCR

## Step 3: Basic Translation 
- usage of huggingface NLP model to test japanese to english translation
- planning to add more languages
- transformer pipeline requires sentencepiece
- sentencepiece is incompatible with python 3.13 at this time
- resolution to sentencepiece incompatibility is to install cmake 3.27

# Step 4: Combining all into single code and testing
- called Capture
- called OCR
- called Translate
- purpose works as of now