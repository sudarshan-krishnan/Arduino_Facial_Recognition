import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

# Initialize the video capture and the detector
cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('/dev/cu.usbmodem11101', 9600)

while True:
    # Read a new frame from the video capture
    success, frame = cap.read()

    # Check if the frame was captured successfully
    if success:
        # Detect faces in the frame
        img, bboxes = detector.findFaces(frame)

        # Display the frame with detected faces
        cv2.imshow("Video", img)

        # Check for the 'q' key to break out of the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to capture frame")
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
