from services.RecordingService import RecordingService
from services.QueueRecordService import QueueRecordService
from factories.RecordingServiceFactory import RecordingServiceFactory


class RecordingController :
    recording_service_factory: RecordingServiceFactory
    queue_record_service: QueueRecordService
    recording_service: RecordingService
    def __init__(self, recording_service_factory: RecordingServiceFactory, queue_record_service: QueueRecordService) -> None:
        self.recording_service_factory = recording_service_factory
        self.queue_record_service = queue_record_service
        self.recording_service = None
        # record can be used like this here as this is not multi tenant since it is one unique device

    def stop_record(self):
        if self.recording_service:
            self.recording_service.stop_recording()
            record_path = self.recording_service.get_file_name()
            self.recording_service = None
            self.queue_record_service.notify_record_ready_for_upload(record_path)


    def record_frame(self,frame):
        if self.recording_service is None:
            self.recording_service = self.recording_service_factory.create_new_recording()
        self.recording_service.add_frame(frame)
        