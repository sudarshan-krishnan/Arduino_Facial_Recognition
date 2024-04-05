import cv2
from cvzone.FaceDetectionModule import FaceDetector
import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('/dev/cu.usbmodem11101', 9600)  
time.sleep(2)

# Initialize the webcam and face detector
cap = cv2.VideoCapture(0)  # 0 is the default camera
detector = FaceDetector()

try:
    while True:
        success, img = cap.read()
        if not success:
            break

        # Detect the face
        img, bboxs = detector.findFaces(img, draw=True)

        # If faces are detected, send a signal to unlock
        if bboxs:
            ser.write(b'1')  # Signal to unlock
        else:
            ser.write(b'0')  # Signal to lock

        # Display the image
        cv2.imshow("Face Detection", img)
        cv2.waitKey(1)
finally:
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
