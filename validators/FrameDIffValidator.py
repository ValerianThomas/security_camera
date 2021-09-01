import numpy as np

class FrameDiffValidator:
    def __init__(self, configs, base_file_service):
        self.base_file_service = base_file_service
        self.configs = configs

    
    def is_greater_than_threshold(self, diff_frame):
        min_euclidian_dist = self.configs.get('min_euclidian_dist')
        base_frame = self.base_file_service.base_frame
        return self.euclidian_distance_between_two_images(base_frame, diff_frame) > min_euclidian_dist

    def euclidian_distance_between_two_images(self, frame1, frame2):
        return np.linalg.norm( frame1.flatten() - frame2.flatten() , axis = 1 )