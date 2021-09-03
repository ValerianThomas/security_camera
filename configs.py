import cv2

configs = {
    "camera_resolution":(640, 480),
    "camera_framerate": 32,
    "max_frame_record": 100,
    "video_folder": "/Users/valerian/Documents/IT/Learning/IOT/security_camera/records",
    "frames_to_persist": 200,
    "file_extension":"mp4",
    "video_dimension": (640, 480),
    "kernel_shape": (21,21),
    "cv_grayscaling_color_method": cv2.COLOR_BGR2GRAY,
    "mid_threshold_value": 30,
    "maxtrehshold_value": 255,
    "opencvtreshold_method": cv2.THRESH_BINARY,
    "min_size_contour": 100000,
    "min_euclidian_dist": 0.3,

}