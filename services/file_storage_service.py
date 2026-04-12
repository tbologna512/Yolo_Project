import os
import time
import cv2
from domain.models import TrainingImage


class FileStorageService:
    def __init__(self, base_folder: str = "training_data"):
        self.base_folder = base_folder
        os.makedirs(self.base_folder, exist_ok=True)

    def save_training_image(self, frame, prefix: str = "candy") -> TrainingImage:
        file_name = f"{prefix}_{int(time.time())}.jpg"
        file_path = os.path.join(self.base_folder, file_name)
        cv2.imwrite(file_path, frame)
        return TrainingImage(file_path=file_path)