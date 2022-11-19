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
# Camera Commands
###############################

def go_up(ser):
    ser.write(bytearray([49]))

def go_down(ser):
    ser.write(bytearray([50]))

def go_left(ser):
    ser.write(bytearray([51]))

def go_right(ser):
    ser.write(bytearray([52]))

def go_center(ser):
    ser.write(bytearray([53]))

def go_drive_mode(ser):
    ser.write(bytearray([54]))

def connect_to_camera(port='/dev/ttyACM0'): #needs to be different from the other ones...
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

def initialize_camera():

    ser = connect_to_camera()

    print("Initializing camera to default settings...")
    try:
        #ser.flush()
        go_center(ser)
        print("Finished setup...")
        return ser
    except OSError as e:
        print(e)
        print("Setup failed... Exiting now...\n")
        exit()




class CameraControlSubscriber(Node):

    def __init__(self):
        super().__init__('motor_control_subscriber')
        self.subscription = self.create_subscription(String, 'controls', self.camera_instruct, 10)
        self.subscription  # prevent unused variable warning
        self.ser = initialize_camera()


    def camera_instruct(self, msg):

        self.get_logger().info('I heard: "%s"' % msg.data)
        if msg.data == "1":
            go_up(self.ser)
        elif msg.data == "2":
            go_down(self.ser)
        elif msg.data == "3":
            go_left(self.ser)
        elif msg.data == "4":
            go_right(self.ser)
        elif msg.data == "6":
            go_drive_mode(self.ser)
        else:
            go_center(self.ser)


def main(args=None):
    rclpy.init(args=args)

    camera_control_subscriber = CameraControlSubscriber()

    rclpy.spin(camera_control_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    camera_control_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
