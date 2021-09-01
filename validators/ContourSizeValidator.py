import cv2
class ContourSizeValidator:
    def __init__(self, configs):
        self.configs = configs
    
    def is_greater_than_threshold(self, contour):
        min_size_contour = self.configs.get('min_size_contour')
        return cv2.contourArea(contour) > min_size_contour