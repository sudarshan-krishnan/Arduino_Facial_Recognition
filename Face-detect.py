import cv2
import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('/dev/cu.usbmodem11101', 9600)  
time.sleep(2)

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the camera
cap = cv2.VideoCapture(0)  # 0 is the default camera

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame with rectangles
        cv2.imshow('Face Detection', frame)

        # If at least one face is detected, send a signal to Arduino
        if len(faces) > 0:
            ser.write(b'1')  # Signal to unlock
        else:
            ser.write(b'0')  # Signal to lock

        # Break the loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # When everything done, release the capture and close serial
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
