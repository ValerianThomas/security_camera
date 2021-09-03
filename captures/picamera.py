import time
from picamera.array import PiRGBArray
from picamera import PiCamera

class PiCamera:
    def __init__(self, configs):
        self.configs = configs
        self.camera = PiCamera()
        self.camera.resolution = self.configs.get("camera_resolution")
        self.camera.framerate = self.configs.get("camera_framerate")
        self.rawCapture = PiRGBArray(self.camera, size=self.configs.get("camera_resolution"))

    def __iter__(self):
        return self

    
    def __next__(self):
        frame_array = self.camera.capture_continous(self.rawCapture, format="bgr", use_video_port=True)
        return frame_array.array
       

