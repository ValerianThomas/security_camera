import time
from picamera.array import PiRGBArray
from picamera import PiCamera


class CaptureController:
    def __init__(self, configs, detection_controller, record_controller):
        self.configs = configs
        self.detection_controller = detection_controller
        self.record_controller=record_controller

        # not multi tenant so we can set variables in class with no worries
        self.recorded_frame_counter = 0
        self.should_record = False
        self.camera = PiCamera()
        self.camera.resolution = self.configs.get("camera_resolution")
        self.camera.framerate = self.configs.get("camera_framerate")
        self.rawCapture = PiRGBArray(self.camera, size=self.configs.get("camera_resolution"))


        # allow camera to warmup
        time.sleep(0.2)


    def start_recording(self):
        for frame_array in self.camera.capture_continous(self.rawCapture, format="bgr", use_video_port=True):
            frame = frame_array.array

            if self.should_record == False:
                self.watch_for_changes_in_frame(frame)
            
            else:
                self.record_frame(frame)
        

    def reset_frame_count(self):
        if self.should_record == True:
            self.recorded_frame_counter = 0


    def watch_for_changes_in_frame(self, frame):
        self.should_record = self.detection_controller.shouldStartRecording(frame)
        self.reset_frame_count()

    

    def reset_record(self):
        self.should_record=False
        self.record_controller.stop_rercord()
        

    def record_frame(self, frame):
        self.recorded_frame_counter += 1
        self.record_controller.record_frame(frame)
        if self.recorded_frame_counter >= self.configs.get("max_frame_record"):
            self.reset_record()
