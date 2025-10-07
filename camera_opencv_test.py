#!/usr/bin/env python3
"""
BloomBotanics Camera Test with OpenCV
Takes 5 photos, 2 seconds apart
"""
import cv2
import time
from datetime import datetime

print("📸 BloomBotanics Camera Test (OpenCV)")
print("=" * 50)

# Open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open camera")
    print("💡 Try: sudo modprobe bcm2835-v4l2")
    exit(1)

# Set resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

print("✅ Camera opened!")
print("📷 Taking 5 photos (2 seconds apart)")
print("=" * 50)

try:
    for i in range(1, 6):
        ret, frame = cap.read()
        
        if ret:
            timestamp = datetime.now().strftime('%H%M%S')
            filename = f'camera_test_{i:02d}_{timestamp}.jpg'
            
            cv2.imwrite(filename, frame)
            print(f"[{i}/5] ✅ Saved: {filename}")
            
            time.sleep(2)
        else:
            print(f"[{i}/5] ❌ Failed to capture frame")
            break
            
except KeyboardInterrupt:
    print("\n🛑 Stopped by user")

cap.release()
print("=" * 50)
print("✅ Test complete!")
print("📁 Check files: ls -lh camera_test_*.jpg")

