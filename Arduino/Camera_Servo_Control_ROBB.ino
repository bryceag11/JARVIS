#include <Servo.h>
Servo myservo;
Servo myservo2;
int pos = 90;
int pos2 = 100;

void setup()
{
Serial.begin(9600);

delay(1000);

myservo.attach(9);
myservo2.attach(11);
delay(1000);

myservo.write(pos);
myservo2.write(pos2);
delay(1000);

}
void loop(){

if (Serial.available())
{

int state = Serial.read();
//Serial.println(state);

if(state == 49 && pos2 >= 102){
  //Serial.println("UP!");
  pos2 = pos2 - 2;
  myservo2.write(pos2);
}
else if(state == 49 && pos2 == 100){
  //Serial.println("Can't go up anymore!");
}

if(state == 50 && pos2 <= 178){
  //Serial.println("DOWN!");
  pos2 = pos2 + 2;
  myservo2.write(pos2);
}
else if(state == 50 && pos2 == 180){
  //Serial.println("Can't go down anymore!");
}

if(state == 51 && pos <= 178){
  //Serial.println("LEFT!");
  pos = pos + 2;
  myservo.write(pos);
}
else if(state == 51 && pos == 180){
  //Serial.println("Can't go left anymore!");
}

if(state == 52 && pos >= 2){
  //Serial.println("RIGHT!");
  pos = pos - 2;
  myservo.write(pos);
}
else if(state == 52 && pos == 0){
  //Serial.println("Can't go right anymore!");
}

if(state == 53){
  //Serial.println("Center!");
  if(pos > 90){
    while(pos > 90){
      pos = pos - 2;
      myservo.write(pos);
      delay(100);
    }
  }
  else{
    while(pos < 90){
      pos = pos + 2;
      myservo.write(pos);
      delay(100);
    }
  }
  if(pos2 > 100){
    while(pos2 > 100){
      pos2 = pos2 - 2;
      myservo2.write(pos2);
      delay(100);
    }
  }
  else{
    while(pos2 < 90){
      pos2 = pos2 + 2;
      myservo2.write(pos2);
      delay(100);
    }
  }
}

if(state == 54){
  //Serial.println("Drive mode!");
  if(pos > 90){
    while(pos > 90){
      pos = pos - 2;
      myservo.write(pos);
      delay(100);
    }
  }
  else{
    while(pos < 90){
      pos = pos + 2;
      myservo.write(pos);
      delay(100);
    }
  }
  if(pos2 > 164){
    while(pos2 > 164){
      pos2 = pos2 - 2;
      myservo2.write(pos2);
      delay(100);
    }
  }
  else{
    while(pos2 < 164){
      pos2 = pos2 + 2;
      myservo2.write(pos2);
      delay(100);
    }
  }
}
}
}