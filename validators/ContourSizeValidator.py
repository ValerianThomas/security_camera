import cv2
class ContourSizeValidator:
    def __init__(self, configs):
        self.configs = configs
    
    def is_greater_than_threshold(self, contours):
        min_size_contour = self.configs.get('min_size_contour')
        return any([True if cv2.contourArea(contour) > min_size_contour else False for contour in contours])