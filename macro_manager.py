import cv2  # You need to install this: pip install opencv-python
import time
import os

# Create a folder to save our training images
if not os.path.exists('training_data'):
    os.makedirs('training_data')

def start_camera():
    # Connect to default camera (Index 1)
    cap = cv2.VideoCapture(1)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Macro Manager Iteration 1")
    print("Press 'SPACE' to save a photo (for training).")
    print("Press 'Q' to quit.")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the live feed
        cv2.imshow('Macro Manager - Data Collector', frame)

        # Listen for keyboard presses
        key = cv2.waitKey(1) & 0xFF

        # If Spacebar is pressed, save the image
        if key == ord(' '):
            img_name = f"training_data/candy_{int(time.time())}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"Saved {img_name}!")
        
        # If Q is pressed, quit
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_camera()