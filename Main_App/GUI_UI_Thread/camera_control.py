"""
File Name: camera_control.py

Description: This script provides a class for controlling servo motors to tilt a camera via serial communication. It includes
             methods for moving the camera in different directions, initializing it to default settings,
             and disconnecting from the serial port.

Usage: For use with a camera used for interpersonal communication. Create an instance of the 'CameraControl' class with the desired serial port 
       (default is '/dev/ttyUSB0'). Use the provided methods to control the camera. Make sure to have the 'pyserial' library installed.



Author: Bryce Grant

Class: EE491 (ECE Capstone II)
"""

import serial
import time



class CameraControl:
    def __init__(self):
        self.ser = None

    def connect_to_camera(self, port):
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = port
        self.ser.open()

        if self.ser.is_open:
            print("Successfully connected to port " + port + "\n")
        else:
            print("Failed to connect to port " + port + "\n")
            print("Exiting program...")
            exit()

    def go_up(self):
        try:
            self.ser.write(bytearray([49]))
        except Exception as e:
            print(e)

    def go_down(self):
        try:
            self.ser.write(bytearray([50]))
        except Exception as e:
            print(e)

    def go_left(self):
        try:
            self.ser.write(bytearray([51]))
        except Exception as e:
            print(e)

    def go_right(self):
        try:
            self.ser.write(bytearray([52]))
        except Exception as e:
            print(e)

    def go_center(self):
        try:
            self.ser.write(bytearray([53]))
        except Exception as e:
            print(e)

    def go_drive_mode(self):
        try:
            self.ser.write(bytearray([54]))
        except Exception as e:
            print(e)

    def initialize_camera(self):
        print("Initializing camera to default settings...")
        try:
            self.go_center()
            print("Finished setup...")
        except OSError as e:
            print(e)
            print("Setup failed... Exiting now...\n")
            exit()

    def disconnect(self):
        if self.ser.is_open:
            self.ser.close()
            print("Serial port closed.")
        else:
            print("Serial port was not open.")

    def __del__(self):
        self.disconnect()
