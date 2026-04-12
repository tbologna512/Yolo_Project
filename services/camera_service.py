import cv2


class CameraService:
    def __init__(self, source: int | str = 0):
        self.source = source
        self.cap = None

    def open(self) -> bool:
        self.cap = cv2.VideoCapture(self.source)
        return self.cap.isOpened()

    def get_frame(self):
        if self.cap is None:
            return False, None
        return self.cap.read()

    def set_resolution(self, width: int, height: int) -> None:
        if self.cap is not None:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def release(self) -> None:
        if self.cap is not None:
            self.cap.release()
            self.cap = None