# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#used for motor commands
import time
import serial

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

###############################
# Motor Commands
###############################

#motor 1 or both depending on mode
def set_speed1(ser, speed):
    ser.write(bytearray([0, 49, speed]))
    
#motor 2 or turn value depending on mode
def set_speed2(ser, speed):
    ser.write(bytearray([0, 50, speed]))

# 0 (reverse), 128 (stop), 255 (forward), individual motor controls
def set_mode0(ser):
    ser.write(bytearray([0, 52, 0]))

#set encoder values back to 0
def zero_encoders(ser):
    ser.write(bytearray([0, 53]))

def disable_regulator(ser):
    ser.write(bytearray([0, 54]))

def enable_regulator(ser):
    ser.write(bytearray([0, 55]))

#motors timeout after 2 seconds if no command has been received via UART
def disable_timeout(ser):
    ser.write(bytearray([0, 56]))

def enable_timeout(ser):
    ser.write(bytearray([0, 57]))

###############################
# Motor Setup/Initialization
###############################

def connect_to_motors(port='/dev/ttyUSB0'):
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
        enable_timeout(ser)
        set_mode0(ser)
        zero_encoders(ser)
        print("Finished setup...")
    except:
        print("Setup failed... Exiting now...\n")
        exit()

#stops motors immediately
def stop_now(ser):
    ser.flush()
    #set_speed1(ser, 128)
    #set_speed2(ser, 128)

#takes speeds between 0-100
def go_forward(ser, speed):

    motor_speed = int((speed/100) * 127) + 128
    print("Going Forwards... Before: " + str(speed) + " , After: " + str(motor_speed))

    #set_speed1(ser, motor_speed)
    #set_speed2(ser, motor_speed)

#takes speeds between 0-100
def go_backward(ser, speed):

    motor_speed = int(((100-speed)/100) * 128)
    print("Going Backwards... Before: " + str(speed) + " , After: " + str(motor_speed))

    #set_speed1(ser, motor_speed)
    #set_speed2(ser, motor_speed)

#takes speeds between 0-100
def turn_left(ser, speed):

    forward_speed = int(((100-speed)/100) * 128)
    backward_speed = int((speed/100) * 127) + 128

    print("Turning Left... Before: " + str(speed) + " , After: F: " + str(forward_speed) + " , B: " + str(backward_speed))

    #set_speed1(ser, forward_speed)
    #set_speed2(ser, backward_speed)

#takes speeds between 0-100
def turn_right(ser, speed):

    forward_speed = int(((100-speed)/100) * 128)
    backward_speed = int((speed/100) * 127) + 128

    print("Turning Right... Before: " + str(speed) + " , After: F: " + str(forward_speed) + " , B: " + str(backward_speed))

    #set_speed1(ser, forward_speed)
    #set_speed2(ser, backward_speed)



class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'controls', self.motor_instruct, 10)
        self.subscription2 = self.create_subscription(String, 'objects', self.object_detected, 10)
        self.subscription  # prevent unused variable warning
        self.subscription2 # prevent unused variable warning
        self.object_detected = "0"

    def object_detected(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.object_detected = msg.data

    def motor_instruct(self, msg):
        ser = 0 #placeholder

        if self.object_detected == "0":

            #self.get_logger().info('I heard: "%s"' % msg.data)
            if msg.data == "W":
                go_forward(ser, 50)
                #self.get_logger().info('Going forward')
            elif msg.data == "A":
                turn_left(ser, 50)
            elif msg.data == "D":
                turn_right(ser, 50)
            elif msg.data == "S":
                go_backward(ser, 50)
            else:
                stop_now()
        else:
            self.get_logger().info('Object Detected... pausing for 2 seconds...')
            time.sleep(2)



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
