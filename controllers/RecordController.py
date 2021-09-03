class RecordingController :
    def __init__(self, recording_service_factory) -> None:
        self.recording_service_factory = recording_service_factory
        self.recording_service = None
        # record can be used like this here as this is not multi tenant since it is one unique device

    def stop_record(self):
        if self.recording_service:
            self.recording_service.stop_recording()
            self.recording_service = None


    def record_frame(self,frame):
        if self.recording_service is None:
            self.recording_service = self.recording_service_factory.create_new_recording()
        self.recording_service.add_frame(frame)
        