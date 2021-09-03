from services.VideoConfigService import VideoConfigService
from captures.opencv import OpenCVCapture
from validators.ContourSizeValidator import ContourSizeValidator
from services.FrameDivergenceService import FrameDivergenceService
from utils.ThresholdService import ThresholdService
from utils.GrayScalingService import GrayScalingService
from services.BaseFileService import BaseFileService
from services.RecordingService import RecordingService
from factories.RecordingServiceFactory import RecordingServiceFactory
from controllers.RecordController import RecordingController
from controllers.DetectionController import DetectionController
from controllers.CaptureController import CaptureController
from configs import configs
import uuid

video_config_service = VideoConfigService()

capture_system = OpenCVCapture(0, video_config_service)

gray_scale_util = GrayScalingService(configs)
thresholder_util = ThresholdService(configs)

base_file_service = BaseFileService(thresholder_util, configs)

contour_size_validator = ContourSizeValidator(configs)

frame_divergence_service = FrameDivergenceService(base_file_service, thresholder_util)
recording_service_factory = RecordingServiceFactory(configs, RecordingService, uuid, video_config_service)


record_controller = RecordingController(recording_service_factory)
detection_controller = DetectionController(frame_divergence_service, base_file_service, contour_size_validator, gray_scale_util)
capture_controller = CaptureController(configs, detection_controller, record_controller, capture_system, base_file_service)

capture_controller.start_recording()