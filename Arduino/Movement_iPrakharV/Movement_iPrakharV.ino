#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int pos = 0;    // variable to store the servo position
int incomingByte = 0;  // for incoming serial data

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9
  Serial.begin(9600);  // opens serial port, sets data rate to 9600 bps
}

void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // if '1' is received, unlock
    if (incomingByte == '1') {
      myservo.write(90);  // rotate servo to 90 degrees (adjust as needed)
    }

    // if '0' is received, lock
    if (incomingByte == '0') {
      myservo.write(0);  // rotate servo back to 0 degrees (adjust as needed)
    }
  }
}
