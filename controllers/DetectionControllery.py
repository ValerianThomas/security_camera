class DetectionController:
    def __init__(self, frame_divergence_service, base_file_service, frame_diff_validator, contour_size_validator):
        self.frame_divergence_service = frame_divergence_service
        self.base_file_service = base_file_service
        self.frame_diff_validator = frame_diff_validator
        self.contour_size_validator = contour_size_validator

    def shouldStartRecording(self, frame):
        self.base_file_service.set_base_image(frame)
        diff_frame = self.frame_divergence_service.get_frame_diff(frame)
        if self.frame_diff_validator.is_greater_than_threshold(diff_frame) :
            # first testing euclidan distance before doing heavy calc
            contour = self.frame_divergence_service.get_diff_contour(diff_frame)
            return self.contour_size_validator.is_greater_than_threshold(contour)
        else :
            return False

