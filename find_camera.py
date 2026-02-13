import cv2

def list_cameras():
    # Test the first 5 indexes
    for index in range(5):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera found at Index {index}")
            ret, frame = cap.read()
            if ret:
                print(f" - It works! (Resolution: {frame.shape[1]}x{frame.shape[0]})")
            else:
                print(" - It opened, but returned no image.")
            cap.release()
        else:
            print(f"No camera at Index {index}")

if __name__ == "__main__":
    list_cameras()