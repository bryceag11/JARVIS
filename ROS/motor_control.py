
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
        print("Finished setup...")
    except:
        print("Setup failed... Exiting now...\n")
        exit()

#stops motors immediately
def stop_now(ser):
    ser.flush()
    m.set_speed1(ser, 128)
    m.set_speed2(ser, 128)

#takes speeds between 0-100
def go_backward(ser, speed):

    motor_speed = int(((100-speed)/100) * 128)
    print("Going Backwards... Before: " + str(speed) + " , After: " + str(motor_speed))

    m.set_speed1(ser, motor_speed)
    m.set_speed2(ser, motor_speed)

#takes speeds between 0-100
def go_forward(ser, speed):

    motor_speed = int((speed/100) * 127) + 128
    print("Going Forwards... Before: " + str(speed) + " , After: " + str(motor_speed))

    m.set_speed1(ser, motor_speed)
    m.set_speed2(ser, motor_speed)

#takes speeds between 0-100
def turn_left(ser, speed):

    forward_speed = int(((100-speed)/100) * 128)
    backward_speed = int((speed/100) * 127) + 128

    print("Turning Left... Before: " + str(speed) + " , After: F: " + str(forward_speed) + " , B: " + str(backward_speed))

    m.set_speed1(ser, forward_speed)
    m.set_speed2(ser, backward_speed)

#takes speeds between 0-100
def turn_right(ser, speed):

    forward_speed = int(((100-speed)/100) * 128)
    backward_speed = int((speed/100) * 127) + 128

    print("Turning Right... Before: " + str(speed) + " , After: F: " + str(forward_speed) + " , B: " + str(backward_speed))

    m.set_speed1(ser, forward_speed)
    m.set_speed2(ser, backward_speed)

def test_stop_now(ser, seconds):
    for i in range(seconds):
        stop_now(ser)
        time.sleep(1)

def test_forward(ser, speed, seconds):
    for i in range(seconds):
        go_forward(ser, speed)
        time.sleep(1)
    stop_now(ser)

def test_backward(ser, speed, seconds):
    for i in range(seconds):
        go_backward(ser, speed)
        time.sleep(1)
    stop_now(ser)

def test_turn_right(ser, speed, seconds):
    
    for i in range(seconds):
        turn_right(ser, speed)
        time.sleep(1)
        print(str(i) + " seconds...")
    stop_now(ser)

def test_turn_left(ser, speed, seconds):
    
    for i in range(seconds):
        turn_left(ser, speed)
        print(str(i) + " seconds...")
        time.sleep(1)
    stop_now(ser)

def get_instruction():
    



#def nav():
#    #new thread
#    a = get_instruction()
#    #reset a
#    if a:
#        #case based on a
#        if not object_detected():
#            #allow all cases
#        else:
#            #allow turning only
#            #send feedback to server...




#main
port = '/dev/ttyUSB0'
ser = connect_motors(port)
initialize_motors(ser)

time.sleep(10)

test_forward(ser, 50, 10)
test_stop_now(ser, 5)
test_backward(ser, 50, 10)
test_stop_now(ser, 5)
#test_turn_right(ser, 25, 7.8)
#test_stop_now(ser, 5)
#test_turn_left(ser, 25, 3.9)
#test_stop_now(ser, 5)



ser.close()
exit()