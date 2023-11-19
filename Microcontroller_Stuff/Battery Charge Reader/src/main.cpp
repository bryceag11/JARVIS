#include <Arduino.h>
float resistor1 = 976000;
float resistor2 = 98500;
const float referenceVolts = 5; // the default reference on a 5-volt board
const int batteryPin = A0;         // battery is connected to analog pin 0
float voltageBattery[10];
int count = 1;
int index = 0;

void setup(){
Serial.begin(9600);
}

int findCharge(float battery_voltage) {
  int battery_percentage;
  if (battery_voltage <= 45.5) {
      battery_percentage = 0;
  } else if(battery_voltage <= 46.04) {
      battery_percentage = 10;
  } else if(battery_voltage <= 46.64) {
      battery_percentage = 20;
  } else if(battery_voltage <= 47.24) {
      battery_percentage = 30;
  } else if(battery_voltage <= 47.84) {
      battery_percentage = 40;
  } else if(battery_voltage <= 48.40) {
      battery_percentage = 50;
  } else if(battery_voltage <= 48.96) {
      battery_percentage = 60;
  } else if(battery_voltage <= 49.48) {
      battery_percentage = 70;
  } else if(battery_voltage <= 50) {
      battery_percentage = 80;
  } else if(battery_voltage <= 50.48) {
      battery_percentage = 90;
  } else if(battery_voltage <= 50.92) {
      battery_percentage = 100;
  } else if(battery_voltage >= 50.92) {
      battery_percentage = 100;
  }
  return battery_percentage;
} 

void loop(){
  int value = analogRead(batteryPin); // read the value from the sensor 
  float voltageReading = (value / 1024.0) * referenceVolts; // calculate the ratio to find the voltage aross resistor 2
  voltageBattery[index] = voltageReading * ((resistor1 + resistor2) / resistor2); //calculate voltage of battery with a voltage divider
  voltageBattery[index] = voltageBattery[index] * (5.0/4.9); //adjust for innaccuracies in measurements.

  //find average voltage reading
  float sum = 0;
  for (int i = 0; i < count; i++){
    sum += voltageBattery[i];
  }
  float voltageBatteryAvg = (sum / count);

  // print the battery charge
  //Serial.println(voltageReading);
  //Serial.println(voltageBattery[index]);
  //Serial.println(voltageBatteryAvg);
  Serial.println(findCharge(voltageBatteryAvg));

  //increment count and max out at 100 readings
  if (count < 10){
    count++;
  }

  //increment index and reset the index to 0 when it reaches 100 readings
  if (index < 9){
    index++;
  }
  else{
    index = 0;
  }

  delay(500);
  }