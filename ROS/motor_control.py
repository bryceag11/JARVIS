
import serial
import time
import motor_commands as m

def connect_motors(port):
    
    #open serial port 9600 baud, 8, N, 1 (no timeout)
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = port
    ser.open()

    #check if serial port is open
    if ser.is_open:
        print("Successfully connected to port " + port + "\n")
    else:
        print("Failed to connect to port " + port + "\n")
        print("Exiting program...")
        exit()
    return ser

def initialize_motors(ser):
    print("Initializing motors to default settings...")
    try:
        ser.flush()
        m.enable_timeout(ser)
        m.set_mode0(ser)
        m.zero_encoders(ser)
        #voltage = m.get_voltage(ser)
        #print("Voltage is at " + voltage + "V\n")
        print("Finished setup...")
    except:
        print("Setup failed... Exiting now...")
        exit()

def stop_now(ser):
    ser.flush()
    m.set_speed1(ser, 128)
    m.set_speed2(ser, 128)

#takes speeds between 1-100
def go_backward(ser, speed):
    if speed > 0 and speed <= 100:
        print("Driving forwards at " + str(speed) + "% speed")
        speed = int((speed/100) * 128 - 1)
        m.set_speed1(ser, speed)
        m.set_speed2(ser, speed)

#takes speeds between 1-100
def go_forward(ser, speed):
    if speed > 0 and speed <= 100:
        print("Driving backwards at " + str(speed) + "% speed")
        speed = 128 + int((speed/100) * 128 - 1)
        m.set_speed1(ser, speed)
        m.set_speed2(ser, speed)

def turn_right(ser, speed):
    if speed > 0 and speed <= 100:
        print("Turning right at " + str(speed) + "% speed")
        speed = int((speed/100) * 128 - 1)
        m.set_speed1(ser, speed)
        m.set_speed2(ser, (128+speed))

def turn_left(ser, speed):
    if speed > 0 and speed <= 100:
        print("Turning left at " + str(speed) + "% speed")
        speed = int((speed/100) * 128 - 1)
        m.set_speed1(ser, (128+speed))
        m.set_speed2(ser, speed)


#main
port = '/dev/ttyUSB0'
ser = connect_motors(port)
initialize_motors(ser)

#go forward for 5 seconds
for i in range(5):
    go_forward(ser, 0)
    time.sleep(1)
stop_now(ser)

#go backward for 10 seconds
for i in range(5):
    go_backward(ser, 50)
    time.sleep(1)
stop_now(ser)

#turn right for 5 seconds
for i in range(10):
    turn_right(ser, 75)
    time.sleep(1)
stop_now(ser)

#turn left for 5 seconds
for i in range(10):
    turn_left(75)
    time.sleep(1)
stop_now(ser)


ser.close()
exit()