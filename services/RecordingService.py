import cv2

class RecordingService:
    def __init__(self, configs, filename):
        self.configs = configs
        self.out = cv2.VideoWriter(filename, configs.get('file_extension'), 25, configs.get('video_dimension'))
    
    def add_frame (self, frame):
        self.out.write(frame)
    
    def stop_recording (self, frame):
        self.out.release()
