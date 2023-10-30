#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos;    // variable to store the servo position

void setup() {
 myservo.attach(10);  // attaches the servo on pin 9 to the servo object

 Serial.begin(9600);
 Serial.setTimeout(15);
}
/* ok
void loop() { 
 if (Serial.available()){
    //pos = Serial.readString().toInt(); 
    pos = Serial.parseInt(); 
    Serial.print(pos);
    delay(50);    
    myservo.write(pos);    
 } 
}
*/

void loop() { 
 if (Serial.available()){
    //pos = Serial.readString().toInt(); 
    pos = Serial.parseInt(); 
    delay(15);
    myservo.write(pos);    
    delay(15);
    Serial.print(pos);
    //delay(15);
 } 
} 
