import cv2

class ThresholdService:
    def __init__(self, configs):
        self.configs = configs
    
    def apply_treshold(self, frame):
        mid_threshold_value = self.configs.get("mid_threshold_value")
        maxtrehshold_value = self.configs.get("maxtrehshold_value")
        opencvtreshold_method = self.configs.get("opencvtreshold_method")
        return cv2.threshold(frame, mid_threshold_value, maxtrehshold_value, opencvtreshold_method)[1]
    