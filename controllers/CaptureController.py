import time
from services.BaseFileService import BaseFileService


class CaptureController:
    base_file_service: BaseFileService
    def __init__(self, configs, detection_controller, record_controller, capture_system, base_file_service: BaseFileService):
        self.configs = configs
        self.detection_controller = detection_controller
        self.record_controller=record_controller
        self.base_file_service=base_file_service

        # not multi tenant so we can set variables in class with no worries
        self.recorded_frame_counter = 0
        self.should_record = False
        self.frames = iter(capture_system)

        # allow camera to warmup
        time.sleep(2)        


    def start_recording(self):
        for frame in self.frames:
            print("new frame")
            if frame is None:
                print("empty frame")
                self.record_controller.stop_record()
                break
            print(f"should record {self.should_record}")
            if self.should_record == False:
                self.watch_for_changes_in_frame(frame)
            
            else:
                self.record_frame(frame)
        
        


    def watch_for_changes_in_frame(self, frame):
        self.should_record = self.detection_controller.shouldStartRecording(frame)
        if self.should_record == True:
            self.recorded_frame_counter = 0

    

    def reset_record(self):
        self.should_record=False
        self.record_controller.stop_record()

        

    def record_frame(self, frame):
        self.recorded_frame_counter += 1
        self.record_controller.record_frame(frame)
        print(f"frame count {self.recorded_frame_counter}, max {self.configs.get('max_frame_record')}" )
        if self.recorded_frame_counter >= self.configs.get("max_frame_record"):
            # force reseting the initial frame before recording to detect additional
            self.base_file_service.base_image = None
            self.reset_record()
