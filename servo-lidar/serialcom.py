# Importing Libraries
import serial
import time
#arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=.1)
# arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=.1)

# #115200
# print("waiting for connection...")
# time.sleep(0.5)

# def write_read(x):

#     arduino.write(bytes(str(x), 'utf-8'))
#     #arduino.write( str(x).encode() )
#     time.sleep(0.05 )
#     data = arduino.readline()
#     return data

pos=1
vers=1

while True:
    # Taking input from user
    # pos = input("Enter a number: ") 

    bpos = write_read(pos)
    ipos = bpos.decode()                      # 256

    print(bpos,ipos) # printing the value

    pos += vers
    
    if pos < 1 or pos >= 180: 
        vers *= -1 

    time.sleep(0.050)
    #time.sleep(0.0)


