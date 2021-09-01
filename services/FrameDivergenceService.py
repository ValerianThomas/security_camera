import cv2
class FrameDivergenceService:
    def __init__(self, threshold_util, base_file_service,gray_scaling_service, config):
        self.threshold_util = threshold_util
        self.config = config
        self.base_file_service = base_file_service
        self.gray_scaling_service = gray_scaling_service

    def get_frame_diff(self, frame):
        gray = self.gray_scaling_service.apply_gray_scale(frame)
        gray = self.threshold_util.apply_treshold(frame)
        return cv2.absdiff(self.base_file_service.base_image, gray)

    
    def get_diff_contour(self, frame):
        diff = self.get_diff_contour(frame)
        dilated_diff = cv2.dilate(diff, None, iterations=0)
        contour,_ = cv2.findContours(dilated_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contour

