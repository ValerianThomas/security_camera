from services.VideoConfigService import VideoConfigService
import cv2


class RecordingService:
    video_config_service: VideoConfigService

    def __init__(self, filename: str, video_config_service: VideoConfigService):
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.filename = filename
        self.video_config_service = video_config_service
        self.out = cv2.VideoWriter(
            filename,
            self.fourcc,
            self.video_config_service.get_video_fps(),
            (
                self.video_config_service.get_video_width(),
                video_config_service.get_video_height(),
            ),
        )

    def add_frame(self, frame):
        self.out.write(frame)

    def stop_recording(self):
        self.out.release()

    def get_file_name(self):
        return self.filename
