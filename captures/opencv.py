from services.VideoConfigService import VideoConfigService
import cv2


class OpenCVCapture:
    video_config_service: VideoConfigService

    def __init__(self, filepath, video_config_service: VideoConfigService):
        self.capture = cv2.VideoCapture(filepath)
        self.video_config_service = video_config_service
        self.set_capture_metadata()

    def set_capture_metadata(self):
        video_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        video_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = self.capture.get(cv2.CAP_PROP_FPS)

        self.video_config_service.set_video_fps(fps)
        self.video_config_service.set_video_height(video_height)
        self.video_config_service.set_video_width(video_width)

    def __iter__(self):
        return self

    def __next__(self):
        _sucess, img = self.capture.read()
        if _sucess:
            return img
        else:
            StopIteration
