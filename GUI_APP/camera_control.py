"""
File: motor_commands.py
Author: Bryce Grant
Class: EE 491 (ECE Capstone II)
Description: CameraControl class with methods for control of the camera servo motor
"""
import serial
import time
import motor_commands as m



class CameraControl:
    def __init__(self, port='COM4'):
        self.ser = None
        self.connect_to_camera(port)

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
