#include <Servo.h>

Servo servoMotor;
int servoPin = 9;
int pos = 0;

int ledPin = 13;
bool faceDetected = false;

void setup() {
  servoMotor.attach(servoPin);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino initialized"); // Print initialization message
}

void loop() {
  if (Serial.available() > 0) {
    int state = Serial.read();
    if (state == '1') {
      faceDetected = true;
    } else {
      faceDetected = false;
    }
  }

  if (faceDetected) {
    servoMotor.write(90);
    delay(15);
    digitalWrite(ledPin, HIGH);
    Serial.println("Face detected, servo at 90 degrees, LED on"); // Print stage
  } else {
    servoMotor.write(0);
    delay(15);
    digitalWrite(ledPin, LOW);
    Serial.println("No face detected, servo at 0 degrees, LED off"); // Print stage
  }
}
