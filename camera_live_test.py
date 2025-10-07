#!/usr/bin/env python3
"""
Live Camera Test - Works without raspistill
"""
import time
from datetime import datetime

print("📸 BloomBotanics Live Camera Test")
print("=" * 50)

try:
    from picamera import PiCamera
    
    # Initialize
    camera = PiCamera()
    camera.resolution = (1920, 1080)
    
    print("✅ Camera initialized (1920x1080)")
    
    # Warm up
    print("⏳ Warming up camera (2 seconds)...")
    camera.start_preview()
    time.sleep(2)
    
    # Capture
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'LIVE_TEST_{timestamp}.jpg'
    
    print(f"📷 Capturing: {filename}")
    camera.capture(filename)
    
    # Stop preview
    camera.stop_preview()
    camera.close()
    
    print(f"✅ SUCCESS! Photo saved!")
    
    # Show details
    import os
    size = os.path.getsize(filename)
    print(f"📁 Location: ~/Desktop/BloomBotanics/{filename}")
    print(f"📊 File size: {size:,} bytes ({size/1024:.1f} KB)")
    
    print("=" * 50)
    print("🎉 Camera is WORKING PERFECTLY!")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()

