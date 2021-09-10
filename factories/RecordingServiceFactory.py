from services.RecordingService import RecordingService
from services.VideoConfigService import VideoConfigService


class RecordingServiceFactory:
    video_config_service: VideoConfigService
    RecordingServiceClass: RecordingService

    def __init__(
        self,
        configs,
        RecordingServiceClass: RecordingService,
        uuid_generator,
        video_config_service: VideoConfigService,
    ):
        self.configs = configs
        self.RecordingServiceClass = RecordingServiceClass
        self.uuid_generator = uuid_generator
        self.video_config_service = video_config_service

    def _generate_filename(self):
        folder_path = self.configs.get("video_folder")
        file_extension = self.configs.get("file_extension")
        return f"{folder_path}/{self.uuid_generator()}.{file_extension}"

    def create_new_recording(self):
        return self.RecordingServiceClass(
            self._generate_filename(), self.video_config_service
        )
