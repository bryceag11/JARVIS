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


# setting visualization parameters
pos=0
vers=1
v3dr=180
pos_init= 0
pos_end = 32
pos_step=2
lidar_chunk_size=1280*2
dist_limit=2000

# setting control parameters
speed = 25
direction = 0.0 # direction in degrees
increment_turn = 0.4

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

'''
Drive function for motor thread
'''
def drive():
    global motor_thread_run

    while motor_thread_run:
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

        # ... (previous code for calculating averages and coordinates remains unchanged)

        # Assuming left_lidar_data and right_lidar_data contain data from left and right lidar respectively
        left_lidar_data = []  # Replace with actual left lidar data
        right_lidar_data = []  # Replace with actual right lidar data

        # Check if an object is detected within 900mm in front
        if center_average < 900:
            # Stop the rover
            motor.stop_motors(ser)

            # Determine whether to turn left or right based on left and right lidar data
            if max(left_lidar_data) > max(right_lidar_data):
                # Turn right
                motor.turn_right(ser, speed)
            else:
                # Turn left
                motor.turn_left(ser, speed)
        else:
            # Convert radians to degrees and ensure it's within [0, 360)
            direction = sum_angle * (180 / math.pi) % 360

            # Continue normal movement based on calculated direction
            motor.go_dir(ser, speed, direction)
        
        time.sleep(0.2)  # delay for processing stability
    # cleanup and stop motor with false flag 
    motor.stop_motors(ser)

'''
Main function for data processing and motor control
'''
def main():
    global direction
    try:
        if(Obj.Connect()): # establish connection to LiDAR device
            print(Obj.GetDeviceInfo())
            gen = Obj.StartScanning() 
            threading.Thread(target=drive).start() # start motor control thread
        else:
            print("Error connecting to device")

        while True:
            data = next(gen)

            pass

    except (KeyboardInterrupt, SystemExit):
        print("Quitting")

        # set the motor thread flag false
        motor_thread_run = False

        # stop motors if not already stopped
        motor.stop_motors(ser)

        # disconnect the lidar
        Obj.StopScanning() 
        Obj.Disconnect()
