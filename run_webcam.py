import argparse
import cv2

from services.camera_service import CameraService
from services.yolo_inference_service import YoloInferenceService
from controllers.scan_controller import ScanController


def parse_source(src: str):
    s = src.strip().lower()
    if s.startswith("usb") and s[3:].isdigit():
        return int(s[3:])
    if s.isdigit():
        return int(s)
    return src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="models/my_model.pt",
                    help="Path to model weights (default: models/my_model.pt)")
    ap.add_argument("--source", default="usb0",
                    help="usb0/usb1/usb2, a camera index (0/1/2), or a file path")
    ap.add_argument("--imgsz", type=int, default=640,
                    help="Inference image size (default: 640)")
    args = ap.parse_args()

    source = parse_source(args.source)

    camera_service = CameraService(source)
    if not camera_service.open():
        print("Error: Could not open webcam or source.")
        return

    inference_service = YoloInferenceService(args.model, imgsz=args.imgsz)
    scan_controller = ScanController(camera_service, inference_service)

    print("Macro Manager OOP Refactor - Webcam Inference")
    print("Press 'Q' to quit.")

    while True:
        ret, frame = scan_controller.get_next_frame()
        if not ret:
            print("Failed to grab frame")
            break

        detections = scan_controller.process_frame(frame)

        y_offset = 30
        for detection in detections:
            text = f"{detection.label} ({detection.confidence:.2f})"
            cv2.putText(
                frame,
                text,
                (10, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )
            y_offset += 30

        cv2.imshow("Macro Manager - Webcam Inference", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    camera_service.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()