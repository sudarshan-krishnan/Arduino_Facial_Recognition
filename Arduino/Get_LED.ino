#include <cvzone.h>

SerialData serialData(2, 1);  // Assuming SerialData is a class from cvzone library
int valsRec[2];  // Array of int with size numOfValsRec

void setup() {
  pinMode(13, OUTPUT);  // Set the green LED pin to output mode
  pinMode(12, OUTPUT);  // Set the red LED pin to output mode
  serialData.begin();   // Initialize the serial data object
}

void loop() {
  serialData.get(valsRec);    // Receive the data into valsRec array
  digitalWrite(13, valsRec[0]);  // Set the green LED according to valsRec[0]
  digitalWrite(12, valsRec[1]);  // Set the red LED according to valsRec[1]
  delay(10);  // Small delay to debounce
}
