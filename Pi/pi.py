import cv2
import serial

# Initialize the camera
cap = cv2.VideoCapture(0)

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize serial communication for Raspberry Pi Pico
# Make sure to replace '/dev/ttyUSB0' with your actual serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # If at least one face is detected
    if len(faces) > 0:
        # Send command to unlock the door via Raspberry Pi Pico
        ser.write(b'UNLOCK\n')

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
