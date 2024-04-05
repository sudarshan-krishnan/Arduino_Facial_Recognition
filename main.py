import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap=cv2.VideoCapture(0)
detector=FaceDetector()


while True:
    success,frame=cap.read()
    img, bBxoes = detector.findFaces(img)

    cv2.imshow("Video",img)

    cv2.waitKey(1)
