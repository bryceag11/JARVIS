#include <Arduino.h>
#include <Servo.h>

// Servo motor stuff
Servo servo;
int angle = 120; //starting angle
const int servoPin = 8;

// Define pin connections & motor's steps per revolution
const int dirPinHori = 2;
const int stepPinHori = 3;
const int dirPinVert = 4;
const int stepPinVert = 5;
const int LEDpin = 13;
const int stepsPerRevolution = 200;
int stepsPerKeyboardPress = 20;
int stepDelay = 2000;
bool isStreaming = true; //set to false by default

void setup()
{
  // Declare pins as outputs for stepper motors
  pinMode(stepPinHori, OUTPUT);
  pinMode(dirPinHori, OUTPUT);
  pinMode(stepPinVert, OUTPUT);
  pinMode(dirPinVert, OUTPUT);

  Serial.begin(9600); // Initialize the serial communication

  // Declare pin as output for LED
  pinMode(LEDpin, OUTPUT);

  // Declare pin and varaible to control servo motor
  servo.attach(servoPin);
  servo.write(angle);
}

void moveLeft()
{
  digitalWrite(dirPinHori, LOW); // Set direction counterclockwise
  // Spin motor
  for (int i = 0; i < stepsPerKeyboardPress; i++){
  digitalWrite(stepPinHori, HIGH);
  delayMicroseconds(stepDelay);
  digitalWrite(stepPinHori, LOW);
  delayMicroseconds(stepDelay);
  }
}

void moveRight()
{
  digitalWrite(dirPinHori, HIGH); // Set direction clockwise
  // Spin motor
  for (int i = 0; i < stepsPerKeyboardPress; i++){
  digitalWrite(stepPinHori, HIGH);
  delayMicroseconds(stepDelay);
  digitalWrite(stepPinHori, LOW);
  delayMicroseconds(stepDelay);
  }
}

void moveDown()
{
  digitalWrite(dirPinVert, LOW); // Set direction counterclockwise
  // Spin motor
  for (int i = 0; i < stepsPerKeyboardPress; i++){
  digitalWrite(stepPinVert, HIGH);
  delayMicroseconds(stepDelay);
  digitalWrite(stepPinVert, LOW);
  delayMicroseconds(stepDelay);
  }
}

void moveUp()
{
  digitalWrite(dirPinVert, HIGH); // Set direction clockwise
  // Spin motor
  for (int i = 0; i < stepsPerKeyboardPress; i++){
  digitalWrite(stepPinVert, HIGH);
  delayMicroseconds(stepDelay);
  digitalWrite(stepPinVert, LOW);
  delayMicroseconds(stepDelay);
  }
}

// Controls servo motor to change the mode of the camera
void changeMode(){
  // now scan back from 180 to 0 degrees
  for(angle = 120; angle > 87; angle--)    
  {                                
    servo.write(angle);           
    delay(5);       
  } 
  // scan from 0 to 180 degrees
  for(angle = 87; angle < 120; angle++)  
  {                                  
    servo.write(angle);               
    delay(5);                   
  } 
  
}

void loop()
{
  if (Serial.available() > 0) {
    char key = Serial.read();

    // Control horizontal motor
    if (key == 'd') {
      moveRight();
    } else if (key == 'a') {
      moveLeft();
    } else {
      // If no direction is being input is held down, stop the motors
      digitalWrite(stepPinHori, LOW);
    }

    // Control vertical motor
    if (key == 's') {
      moveDown();
    } else if (key == 'w') {
      moveUp();
    } else {
      // If no direction is being input is held down, stop the motors
      digitalWrite(stepPinVert, LOW);
    }

    // Change camera mode
    if (key == 'm'){
      changeMode();
    }
  }

  //check if 
  if (isStreaming){
    digitalWrite(LEDpin, HIGH);  // turn the LED on (HIGH is the voltage level)
  }
  else{
    digitalWrite(LEDpin, LOW);   // turn the LED off by making the voltage LOW
  } 

}