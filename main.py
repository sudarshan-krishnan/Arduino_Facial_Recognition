import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('COM_PORT', 9600)  # Replace 'COM_PORT' with your Arduino's COM port

while True:
    success, frame = cap.read()
    if success:
        img, bboxes = detector.findFaces(frame)
        if bboxes:
            arduino.sendData([1])  # Face detected
        else:
            arduino.sendData([0])  # No face detected
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to capture frame")
        break

cap.release()
cv2.destroyAllWindows()
