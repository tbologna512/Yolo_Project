from services.camera_service import CameraService
from services.file_storage_service import FileStorageService


class CaptureController:
    def __init__(self, camera_service: CameraService, file_storage_service: FileStorageService):
        self.camera_service = camera_service
        self.file_storage_service = file_storage_service

    def capture_current_frame(self):
        ret, frame = self.camera_service.get_frame()
        if not ret:
            return None
        return self.file_storage_service.save_training_image(frame)