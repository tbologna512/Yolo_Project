from services.camera_service import CameraService
from services.yolo_inference_service import YoloInferenceService


class ScanController:
    def __init__(self, camera_service: CameraService, inference_service: YoloInferenceService):
        self.camera_service = camera_service
        self.inference_service = inference_service

    def get_next_frame(self):
        return self.camera_service.get_frame()

    def process_frame(self, frame):
        return self.inference_service.detect(frame)