import serial
import time

#serial device name
dev = '/dev/ttyUSB0'

#open serial port
ser = serial.Serial()
ser.baudrate = 9600
ser.port = dev
ser.open()

if ser.is_open:
    print("Successfully connected to port " + dev + "\n")
else:
    print("Failed to connect to port " + dev)

while True:
  ser.write(0x77)
  time.sleep(1000)
