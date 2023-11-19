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

from Main_App.GUI_UI_Thread.motor_control import MotorCommands
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
ser = motor.connect_motors("dev/ttyUSB0")
motor.initialize_motors(ser)

# setting control parameters
speed = 25
direction = 0.0 # direction in degrees
increment_turn = 0.4

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
        motor.go_dir(ser, speed, direction) # move in the specified direction
        time.sleep(0.2) # delay for processing stability

    # cleanup and stop motor with false flag 
    motor.stop_motors(ser)

'''
Render function for point cloud visualization
'''
def Render(pts):
    glPointSize(2)
    glBegin(GL_POINTS)  
    sc=0.001
    fk = 180-len(pts)

    for i in range(0,len(pts)):
        p = (sc*pts[i][0], sc*pts[i][1], sc*pts[i][2])
        maxlength=1000
        r=cmap(pts[i][2],0,maxlength,0,1)
        g=cmap(pts[i][1],0,maxlength,0,1)
        b=cmap(pts[i][0],0,maxlength,0,1)
        
        glColor3f(b,g,r) 
        glVertex3fv(p)
    glEnd()

def cmap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / float(in_max - in_min) + out_min;

def Rx(theta):
    return np.array([[ 1, 0           , 0           ],
                     [ 0, math.cos(theta),-math.sin(theta)],
                     [ 0, math.sin(theta), math.cos(theta)]])

# Add Ry and Rz functions here

def write_read(x):
    arduino.write(bytes(str(x), 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=.015)
print("//waiting for Serial connection...")
time.sleep(0.5)

# Serial port to which lidar connected, Get it from device manager windows
# In linux type in terminal -- ls /dev/tty* 
# port = input("Enter port name which lidar is connected:") #windows

# Initialize video capture
cap = cv2.VideoCapture(0)

# Video frame processing function
def videocam(frame):
    rfr = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    div = 64 
    quantized = (rfr // div * div) + div // 2
    ksize = (10, 10) 
    quantized = cv2.blur(quantized, ksize) 

    cv2.line(rfr, (0, int(rfr.shape[0]/2)), (int(rfr.shape[1]), int(rfr.shape[0]/2)), (0, 255, 0), 1)
    cv2.line(rfr, (int(rfr.shape[1]/2), 0), (int(rfr.shape[1]/2), int(rfr.shape[0])), (0, 255, 0), 1)

    cv2.imshow('frame', rfr)
    return rfr

# Drive function for motor thread
def drive():
    global motor_thread_run

    while motor_thread_run:
        motor.go_dir(ser, speed, direction) # move in the specified direction
        time.sleep(0.2) # delay for processing stability

    # cleanup and stop motor with false flag 
    motor.stop_motors(ser)

'''
Main function for data processing and motor control
'''
def main():
    global direction
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


try:
    if(Obj.Connect()): # establish connection to LiDAR device
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning() 
        threading.Thread(target=drive).start() # start motor control thread
    else:
        print("Error connecting to device")

    main() # start main processing loop

except (KeyboardInterrupt, SystemExit):
    print("Quitting")

    # set the motor thread flag false
    motor_thread_run = False

    # stop motors if not already stopped
    motor.stop_motors(ser)

    # disconnect the lidar
    Obj.StopScanning() 
    Obj.Disconnect()
