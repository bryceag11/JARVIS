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



# setting control parameters
speed = 25
direction = 0.0 # direction in degrees

# initializing motor commands
motor = MotorCommands()
ser = motor.connect_motors("dev/ttyUSB0")
motor.initialize_motors(ser)


# initialize bins for lidar data
bins=[]
for _ in range (360):  # clear the bins
    bins.append(0)

port = "/dev/ttyUSB1" # define port for the YDLidar X4
Obj = PyLidar3.YdLidarX4(port) #PyLidar3.YDLidarX4(port,chunk_size)

# global flag for motor thread stoppage
motor_thread_run = True
object_detected = False


# Constants for decision-making
STOP_DISTANCE = 900  # Distance threshold to stop the robot in front of an object
BACKWARD_TIME = 0.2  # Time duration to move backward
RIGHT_TURN_DISTANCE = 1000  # Distance threshold to trigger a right turn

'''
Drive function for motor thread
'''
def drive(center_average, left_lidar_data, right_lidar_data):
    global motor_thread_run, object_detected

    # Check if an object is detected in front
    if center_average < STOP_DISTANCE:
        # Set flag for object detected
        object_detected = True

        # Stop the rover
        motor.stop_motors(ser)

        # Check if there are objects all around (left, right, center)
        if all(data < STOP_DISTANCE for data in left_lidar_data) and all(data < STOP_DISTANCE for data in right_lidar_data):
            # Move backward for a specified duration
            motor.go_backward(ser, speed)
            time.sleep(BACKWARD_TIME)
            object_detected = False  # Reset object detection flag after moving backward

            # Check if there's enough space on the right to turn
            if all(data > RIGHT_TURN_DISTANCE for data in right_lidar_data):
                # Turn right
                motor.turn_right(ser, speed)
                time.sleep(1)  # Adjust duration for the turn
                motor.go_forward(ser, speed)  # Resume forward movement

        # Resume normal movement if not all directions are blocked
        else:
            motor.go_forward(ser, speed)

    time.sleep(0.2)  # Delay for processing stability


'''
Main function for data processing and motor control
'''
def main():
    global direction
    global motor_thread_run, object_detected

    while motor_thread_run:
        start_time = time.time()
        while time.time() - start_time < 0.2:

            data = next(gen) # get lidar scan data
            left_total = 0
            right_total = 0
            center_total = 0
            bias = 0
            
            time.sleep(0.2)  # Delay for processing stability
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


        drive(center_average, left_average, right_average)


try:
    if(Obj.Connect()):
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning()
        threading.Thread(target=drive).start()
    else:
        print("Error connecting to device")
    main()
except (KeyboardInterrupt, SystemExit):
    print("Quitting")

    # stop motors if not already stopped
    motor.stop_motors(ser)

    # disconnect the lidar
    Obj.StopScanning()
    Obj.Disconnect()