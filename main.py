import cv2
from cvzone.FaceDetectionModule import FaceDetector
from motor_control import turn_off, turn_on

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, frame = cap.read()
    if success:
        img, bboxes = detector.findFaces(frame)
        if bboxes:
            turn_on()

        else:
            turn_off()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to capture frame")
        break

cap.release()
cv2.destroyAllWindows()
