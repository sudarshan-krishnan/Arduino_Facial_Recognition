#include <Servo.h>

Servo myservo;  
const int inputPin = 2; 

void setup() {
  myservo.attach(9);  
  pinMode(inputPin, INPUT_PULLUP);  
}

void loop() {
 
  int inputValue = digitalRead(inputPin);  

  if (inputValue == LOW) {
    myservo.write(0);
  } 
  
  else if (inputValue == HIGH) {
    myservo.write(90);
  }

  delay(15);  
}
