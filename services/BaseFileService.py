class BaseFileService:
    def __init__(self, thresholder_util, configs):
        self.thresholder_util = thresholder_util
        self.configs = configs
        self.base_image = None
        # this is only applicable as it is not multi-tenant 
        self.frame_counter = 0
        # same here

    def reset_base_image (self, frame):
        self.frame_counter  += 1
        if self.frame_counter > self.configs.get('FRAMES_TO_PERSIST'):
            self.frame_counter = 0
            self.base_image = self.thresholder_util.apply_treshold(frame)

    def set_base_image(self, frame):
        if self.base_image is None:
            self.base_image = frame
