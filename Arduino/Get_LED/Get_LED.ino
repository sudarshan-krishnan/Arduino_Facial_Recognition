#include <Servo.h>

Servo servoMotor;
int servoPin = 9;
int ledPin = 13;
bool faceDetected = false;

void setup() {
  servoMotor.attach(servoPin);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino initialized");
}

void loop() {
  if (Serial.available() > 0) {
    int state = Serial.read();
    faceDetected = (state == '1');
  }




  if (faceDetected) {
    servoMotor.write(90);
    digitalWrite(ledPin, HIGH);
    Serial.println("Face detected, servo at 90 degrees, LED on");
  } else {
    servoMotor.write(0);
    digitalWrite(ledPin, LOW);
    Serial.println("No face detected, servo at 0 degrees, LED off");
  }
  delay(500);
  
}

