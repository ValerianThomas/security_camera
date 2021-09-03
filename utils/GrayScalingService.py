import cv2
class GrayScalingService :
    def __init__(self, configs):
        self.configs = configs
        self.count = 0

    def apply_gray_scale(self, frame):
        kernel_shape = self.configs.get("kernel_shape")
        cv_grayscaling_color_method = self.configs.get("cv_grayscaling_color_method")
        gray = cv2.cvtColor(frame, cv_grayscaling_color_method)
        self.count += 1

        return cv2.GaussianBlur(gray,kernel_shape,0)