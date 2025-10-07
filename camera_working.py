#!/usr/bin/env python3
"""
Working Camera Test - Uses /dev/video0
"""
import cv2
import time
from datetime import datetime

print("📸 BloomBotanics Live Camera Test")
print("=" * 50)

# Open camera (use /dev/video0 - the Pi Camera)
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)

if not cap.isOpened():
    print("❌ Cannot open /dev/video0")
    exit(1)

print("✅ Camera opened successfully!")
print("📷 Taking 3 photos...")
print("=" * 50)

# Wait for camera to initialize
time.sleep(2)

for i in range(1, 4):
    print(f"[{i}/3] Capturing...")
    ret, frame = cap.read()
    
    if ret and frame is not None:
        timestamp = datetime.now().strftime('%H%M%S')
        filename = f'bloom_photo_{i:02d}_{timestamp}.jpg'
        cv2.imwrite(filename, frame)
        
        h, w = frame.shape[:2]
        print(f"[{i}/3] ✅ Saved: {filename} ({w}x{h})")
        time.sleep(1)
    else:
        print(f"[{i}/3] ❌ Failed to capture")

cap.release()
print("=" * 50)
print("✅ Camera test complete!")
print("")
print("📁 View your photos:")
print("   ls -lh bloom_photo_*.jpg")

