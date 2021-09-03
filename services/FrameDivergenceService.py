import cv2
class FrameDivergenceService:
    def __init__(self, base_file_service, threshold_util):
        self.base_file_service = base_file_service
        self.threshold_util = threshold_util

    def get_frame_diff(self, frame):
        return cv2.absdiff(frame, self.base_file_service.base_image) 

    
    def get_diff_contour(self, frame):
        diff = self.get_frame_diff(frame)
        threshold = self.threshold_util.apply_treshold(diff)
        dilated_diff = cv2.dilate(threshold, None, iterations=0)
        contours,_ = cv2.findContours(dilated_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

