'''
from motor_control import MotorCommands
import PyLidar3
import cv2
import numpy as np
import math
import time
import threading
import serial
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class RoverControl:
    def __init__(self):
        speed = 25
        stop_distance = 900
        right_turn_distance = 1000
        backward_time = 0.2

        ser = None
        object_detected = False
        motor = MotorCommands()
        lidar_data = (0, 0, 0)


    def lidar_thread(self):
        port = "/dev/ttyUSB0"
        Obj = PyLidar3.YdLidarX4(port)
        try:
            if Obj.Connect():
                print(Obj.GetDeviceInfo())
                gen = Obj.StartScanning()
                while True:
                    data = next(gen)
                    obst_data= lidar_scan(data)
                    obst_avoid(obst_data)
            else:
                print("Failed to connect to Lidar device.")
        except (KeyboardInterrupt, SystemExit, Error):
            Obj.StopScanning()
            Obj.Disconnect()
            motor.stop_motors()

    def lidar_scan(self, data):
        left_total = 0
        right_total = 0
        center_total = 0
        # measurement and calculation of averages and values
        for angle in range(340,360):  # measure the center
            if(data[angle]> 0):
                center_total = center_total + data[angle]
        for angle in range(0,20):  # measure the center
            if(data[angle]> 0):
                center_total = center_total + data[angle]
        center_average = round(center_total/40,2)
        for angle in range(20,100):  # measure the right side
            if(data[angle]> 0):
                right_total = right_total + data[angle]
        right_average = round(right_total/80,2)
        for angle in range(260,340): # measure the left side
            if(data[angle]> 0):
                left_total = left_total + data[angle]
        left_average = round(left_total/80,2)
        print("Center average", center_average)
        print("Left average", left_average)
        print("Right average", right_average)
        
        # convert to Cartesian coordinates
        left_y = math.sin(math.pi/4) * left_average
        left_x = -1*math.cos(math.pi/4) * left_average
        right_y = math.sin(math.pi/4) * right_average
        right_x = math.cos(math.pi/4) * right_average
        center_y = center_average

        sum_x = round(left_x + right_x,2) # calculate sum of x-coordinates
        sum_y = round(center_y - (left_y + right_y)/2,2) # calculate sum of y-coordinates
        
        if sum_y < 100:
            sum_y = 100  # ensure minimum value for y
        
        # print("Sum x:", sum_x, "Sum y: ", sum_y)

        sum_angle = math.atan2(sum_x,sum_y) # calculate steering angle in radians

        # print ("Sum Steer", round(sum_angle,2))
        return (left_average, center_average, right_average)

   


    def obst_avoid(self, data2):
                lefty, cent, righty = data2  
                if cent < stop_distance:
                    object_detected = True
                    try:
                        motor.stop_motors(ser)
                        if lefty < stop_distance and righty < stop_distance:
                            motor.go_backward(ser, speed)
                            time.sleep(backward_time)
                            object_detected = False

                            if righty > right_turn_distance:
                                motor.turn_right(ser, speed)
                                time.sleep(.2)
                                motor.go_forward(ser, speed)
                            else:
                                motor.turn_left(ser, speed)
                                time.sleep(.2)
                                motor.go_forward(ser, speed)
                        else:
                            motor.go_forward(ser, speed)

                    except Exception as e:
                        print(f"Motor control error: {e}")
                    finally:
                        object_detected = False

    def main(self, lidar_port):
        ser = motor.connect_motors("/dev/ttyUSB1")
        motor.initialize_motors(ser)
        while True:
            lidar_thread()


# Usage example:
if __name__ == "__main__":
    rover = RoverControl()
    try:
        rover.main("/dev/ttyUSB0")
    except (KeyboardInterrupt, SystemExit):
        print("Quitting")

'''

"""
File Name: rover_lidar.py

Description: This script controls motors based on data received from a LiDAR sensor
        to drive autonomous movement through a dynamic window approach (DWA)
        https://github.com/goktug97/DynamicWindowApproach

Usage: Make sure to have the necessary dependencies installed, and provide correct 
       port information for both the motors and the LiDAR device.

Author: Bryce Grant

Class: EE491 (ECE Capstone II)
"""

from motor_control import MotorCommands
import time
import PyLidar3
import math
import threading
import serial
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2
import numpy as np

# initializing motor commands
motor = MotorCommands()
ser = motor.connect_motors("/dev/ttyUSB0")
motor.initialize_motors(ser)

# setting control parameters
speed = 25
direction = 0.0 # direction in degrees
increment_turn = 0.4
stop_distance = 900
right_turn_distance = 1000
backward_time = 0.2
# initialize bins for lidar data
bins=[]
for _ in range (360):  # clear the bins
    bins.append(0)

port = "/dev/ttyUSB1" # define port for the YDLidar X4
Obj = PyLidar3.YdLidarX4(port) #PyLidar3.YDLidarX4(port,chunk_size)

# global flag for motor thread stoppage
motor_thread_run = True
centy = 0
righty = 0
lefty = 0
'''
Drive function for motor thread
'''
def drive():
    global motor_thread_run

    while motor_thread_run:
                if centy < stop_distance:     
                    motor.stop_motors(ser)
                    print("JARVIS detected object{}")
                if lefty < stop_distance and righty < stop_distance:
                    motor.go_backward(ser, speed)
                    time.sleep(backward_time)

                    if righty > right_turn_distance:
                        motor.turn_right(ser, speed)
                        time.sleep(0.2)
                        motor.go_forward(ser, speed)
                    else:
                        motor.turn_left(ser, speed)
                        time.sleep(0.2)
                        motor.go_forward(ser, speed)
                else:
                    motor.go_forward(ser, speed)
    motor.stop_motors(ser)



'''
Main function for data processing and motor control                
            else:
'''
def main():
    global direction, centy, lefty, righty
    while True:
        data = next(gen) # get lidar scan data
        left_total = 0
        right_total = 0
        center_total = 0
        bias = 0
        
        # measurement and calculation of averages and values
        for angle in range(340,360):  # measure the center
            if(data[angle]> 0):
                center_total = center_total + data[angle]
        for angle in range(0,20):  # measure the center
            if(data[angle]> 0):
                center_total = center_total + data[angle]
        center_average = round(center_total/40,2)
        for angle in range(20,100):  # measure the right side
            if(data[angle]> 0):
                right_total = right_total + data[angle]
        right_average = round(right_total/80,2)
        for angle in range(260,340): # measure the left side
            if(data[angle]> 0):
                left_total = left_total + data[angle]
        left_average = round(left_total/80,2)
        print("Center average", center_average)
        print("Left average", left_average)
        print("Right average", right_average)
        
        # convert to Cartesian coordinates
        left_y = math.sin(math.pi/4) * left_average
        left_x = -1*math.cos(math.pi/4) * left_average
        right_y = math.sin(math.pi/4) * right_average
        right_x = math.cos(math.pi/4) * right_average
        center_y = center_average

        sum_x = round(left_x + right_x,2) # calculate sum of x-coordinates
        sum_y = round(center_y - (left_y + right_y)/2,2) # calculate sum of y-coordinates
        
        if sum_y < 100:
            sum_y = 100  # ensure minimum value for y
        
        print("Sum x:", sum_x, "Sum y: ", sum_y)

        sum_angle = math.atan2(sum_x,sum_y) # calculate steering angle in radians

        print ("Sum Steer", round(sum_angle,2))

        # convert radians to degrees and ensure it's within [0, 2π]
        direction = sum_angle * (180 / math.pi) % 360
        sum_dist = math.sqrt(sum_x**2 + sum_y**2)

        righty = right_average
        centy = center_average
        lefty = left_average

try:
    if(Obj.Connect()): # establish connection to LiDAR device
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning() 
        threading.Thread(target=drive).start() # start motor control thread
    else:
        print("Error connecting to device")

    main() # start main processing loop

except (KeyboardInterrupt, SystemExit, Error):
    print("Quitting")

    # set the motor thread flag false
    motor_thread_run = False

    # stop motors if not already stopped
    motor.stop_motors(ser)

    # disconnect the lidarfrom Main_App.GUI_UI_Thread.motor_control import MotorCommands
    Obj.Disconnect()