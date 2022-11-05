
import serial
import time

#serial device name
dev = "/dev/ttyUSB0"

#open serial port
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()

if ser.is_open:
    print("Successfully connected to port " + dev + "\n")
else:
    print("Failed to connect to port " + dev + "\n")
    exit()

 #open serial port 9600 baud, 8, N, 1 (no timeout)

for i in range(10):
    time.sleep(1)
    ser.write(bytearray([0,49,0]))
    ser.write(bytearray([0,50,0]))

ser.close()
exit()

"""
byte read_byte() {
  int count = 100; //max ms delay
  while (count > 0) {
    if (Serial.available() > 0) {
      return Serial.read();
    }
    delay(1);
    count--;
  }
  return 0;
}

void write_byte(byte b) {
  Serial.write(0x00); //Send start byte of 0x00
  Serial.write(b);
}

byte get_speed1() {
  write_byte(0x21);
  return read_byte();
}

byte get_speed2() {
  write_byte(0x22);
  return read_byte();
}

long get_encoder1() {
  write_byte(0x23);
  long result = 0;
  result += (read_byte() << 24);
  result += (read_byte() << 16);
  result += (read_byte() << 8);
  return (result + read_byte());
}

long get_encoder2() {
  write_byte(0x24);
  long result = 0;
  result += (read_byte() << 24);
  result += (read_byte() << 16);
  result += (read_byte() << 8);
  return (result + read_byte());
}

byte get_voltage() {
  write_byte(0x26);
  return read_byte();
}

byte get_current1() {
  write_byte(0x27);
  return read_byte();
}

byte get_current2() {
  write_byte(0x28);
  return read_byte();
}

byte get_version() {
  write_byte(0x29);
  return read_byte();
}

byte get_acceleration() {
  write_byte(0x2A);
  return read_byte();
}

byte get_mode() {
  write_byte(0x2B);
  return read_byte();
}

byte get_error() {
  write_byte(0x2D);
  return read_byte();
}

void set_speed1(byte b) {
  write_byte(0x31);
  Serial.write(b);
}

void set_speed2(byte b) {
  write_byte(0x32);
  Serial.write(b);
}

void set_acceleration(byte b) {
  write_byte(0x33);
  Serial.write(b);
}

//modes range from 0 to 4
void set_mode(byte b) {
  if (b < 5) {
    write_byte(0x34);
    Serial.write(b);
  }
}

void setup() {
  delay(5000);
  Serial.begin(9600);
  Serial.flush();
  set_mode(0x00);
  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:
  for i in range(5):

    set_speed1(0x20);
    set_speed2(0x20);
    delay(4000);
    set_speed1(0x00);
    set_speed2(0x00);
    delay(4000);

  Serial.flush()
  set_speed1(0x00)
  set_speed2(0x00)
  exit()
}
"""
