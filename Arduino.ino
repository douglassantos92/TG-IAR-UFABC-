// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>

// Connect a stepper motor with 48 steps per revolution (7.5 degree)
// to motor port #2 (M3 and M4)
AF_Stepper motor(48, 2);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bp
  motor.setSpeed(20);  // 10 rpm   
}
	
void loop() {
  if (Serial.available()>0){
    if (Serial.read()==116){
    Serial.println("TG III");
    motor.step(3,FORWARD, SINGLE); 
    }
  }
}
