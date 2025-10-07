#!/usr/bin/env python3
"""
Live Camera Preview - 10 seconds
Shows on connected HDMI monitor
"""
from picamera2 import Picamera2, Preview
import time

print("🎬 Starting LIVE Camera Preview")
print("=" * 50)
print("Look at your HDMI monitor!")
print("Preview will run for 10 seconds...")

try:
    camera = Picamera2()
    
    # Configure for preview
    config = camera.create_preview_configuration(main={"size": (1920, 1080)})
    camera.configure(config)
    
    # Start preview on HDMI screen
    camera.start_preview(Preview.QTGL)
    camera.start()
    
    print("▶️  LIVE PREVIEW ACTIVE!")
    print("⏰ Running for 10 seconds...")
    
    # Run for 10 seconds
    time.sleep(10)
    
    # Stop
    camera.stop_preview()
    camera.stop()
    
    print("✅ Preview complete!")
    
except Exception as e:
    print(f"❌ Error: {e}")

