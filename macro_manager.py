import cv2

from services.camera_service import CameraService
from services.file_storage_service import FileStorageService
from controllers.capture_controller import CaptureController


def start_camera():
    camera_service = CameraService(1)

    if not camera_service.open():
        print("Error: Could not open webcam.")
        return

    file_storage_service = FileStorageService("training_data")
    capture_controller = CaptureController(camera_service, file_storage_service)

    print("Macro Manager Iteration 1")
    print("Press 'SPACE' to save a photo (for training).")
    print("Press 'Q' to quit.")

    while True:
        ret, frame = camera_service.get_frame()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Macro Manager - Data Collector", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord(" "):
            training_image = file_storage_service.save_training_image(frame)
            print(f"Saved {training_image.file_path}!")

        elif key == ord("q"):
            break

    camera_service.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()