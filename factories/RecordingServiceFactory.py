class RecordingServiceFactory:
    def __init__(self, configs, RecordingServiceClass, uuid_generator):
        self.configs = configs
        self.RecordingServiceClass = RecordingServiceClass
        self.uuid_generator = uuid_generator

    def _generate_filename(self):
        folder_path = self.configs.get('video_folder')
        file_extension = self.configs.get('file_extension')
        return f"{folder_path}/{self.uuid_generator.uuid4()}.{file_extension}"

    def create_new_recording(self):
        return self.RecordingServiceClass(self.configs,self._generate_filename())


