

class DetectionController:
    def __init__(self, frame_divergence_service, base_file_service, contour_size_validator, gray_scaling_service):
        self.frame_divergence_service = frame_divergence_service
        self.base_file_service = base_file_service
        self.contour_size_validator = contour_size_validator
        self.gray_scaling_service = gray_scaling_service

    def shouldStartRecording(self, frame):
        gray = self.gray_scaling_service.apply_gray_scale(frame)
        self.base_file_service.set_base_image(gray)
        contours = self.frame_divergence_service.get_diff_contour(gray)
        movement = self.contour_size_validator.is_greater_than_threshold(contours)
        if movement:
            print("movement detected...")
    
        return self.contour_size_validator.is_greater_than_threshold(contours)

