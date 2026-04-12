from ultralytics import YOLO
from domain.models import Detection


class YoloInferenceService:
    def __init__(self, model_path: str, imgsz: int = 640):
        self.model = YOLO(model_path)
        self.imgsz = imgsz

    def detect(self, frame) -> list[Detection]:
        results = self.model.predict(frame, imgsz=self.imgsz, verbose=False)

        detections: list[Detection] = []

        for result in results:
            boxes = result.boxes
            if boxes is None:
                continue

            for box in boxes:
                confidence = float(box.conf[0]) if box.conf is not None else 0.0
                class_id = int(box.cls[0]) if box.cls is not None else -1
                label = self.model.names[class_id] if class_id in self.model.names else "unknown"

                detections.append(
                    Detection(
                        confidence=confidence,
                        label=label,
                    )
                )

        return detections