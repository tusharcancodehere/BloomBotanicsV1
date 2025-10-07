"""AI Camera - Disabled"""
class AICamera:
    def __init__(self, *args, **kwargs):
        self.enabled = False
    def start(self): pass
    def capture(self): return None
    def detect_pest(self): return None
    def cleanup(self): pass
