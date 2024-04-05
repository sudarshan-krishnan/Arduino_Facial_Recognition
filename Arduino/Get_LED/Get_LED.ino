#include <Servo.h>

Servo servoMotor; 
int servoPin = 9; 
int pos = 0;      

void setup() {
  servoMotor.attach(servoPin); 
  Serial.begin(9600);          
}

void loop() {
  if (Serial.available() > 0) {
    int state = Serial.read(); 
    if (state == '1') {
      //for (pos = 0; pos <= 90; pos += 1) { 
        servoMotor.write(pos);
        delay(15); 
     // }
   } else {
   //  for (pos = 90; pos >= 0; pos -= 1) { 
       servoMotor.write(0);
       delay(15); 
     }
    }
  }
}
