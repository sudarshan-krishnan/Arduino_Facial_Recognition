import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('/dev/cu.usbmodem11101', 9600)  

while True:
    success, frame = cap.read()
    if success:
        img, bboxes = detector.findFaces(frame)
        if bboxes:
            arduino.sendData([1, 0])
        else:
            arduino.sendData([0, 1])
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to capture frame")
        break

cap.release()
cv2.destroyAllWindows()
