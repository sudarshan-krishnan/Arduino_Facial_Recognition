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
  } else {
    servoMotor.write(0);
    delay(15);
    digitalWrite(ledPin, LOW);
  }
}
