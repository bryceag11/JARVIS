"""
File Name: motor_commands.py

Description: This script provides a class `MotorCommands` for controlling motors through serial communication. 
             It includes methods for motor initialization, setting modes, obtaining motor status, 
             and performing directional movements.

Usage: Usage: For use with RD03 motor drives. Create an instance of the 'MotorCommands' class with the desired serial port 
       (default is '/dev/ttyUSB0'). Use the provided methods to control the motors. Make sure to have the 'pyserial' library installed.
       https://www.robot-electronics.co.uk/rd03-24v-robot-drive.html
       

Author: Bryce Grant

Class: EE491 (ECE Capstone II)

"""

import serial
import threading

class MotorCommands:
    def __init__(self):
        pass  

    '''
    Connects to the specified serial port and returns the serial connection object.
    '''
    def connect_motors(self, port):
        ser = serial.Serial()
        ser.baudrate = 9600 
        ser.port = port
        ser.open()
        
        if ser.is_open:
            print(f"Successfully connected to port {port}\n")
            return ser
        else:
            print(f"Failed to connect to port {port}\n")
            return None
        
    '''
    Initializes the connected motors by setting various modes and configurations
    '''
    def initialize_motors(self, ser):
        try:
            ser.flush()
            self.enable_timeout(ser)
            self.set_mode0(ser)
            self.zero_encoders(ser)
            print("Finished setup...")
        except Exception as e:
            print(f"Setup failed: {e}\n")

    def get_voltage(self, ser):
        ser.write(bytearray([0, 38]))
        return ser.read(1)

    def get_mode(self, ser):
        ser.write(bytearray([0, 43]))
        return ser.read(1)

    def set_speed1(self, ser, speed):
        ser.write(bytearray([0, 49, speed]))

    def set_speed2(self, ser, speed):
        ser.write(bytearray([0, 50, speed]))

    def set_mode0(self, ser):
        ser.write(bytearray([0, 52, 0]))

    def set_mode1(self, ser):
        ser.write(bytearray([0, 52, 1]))

    def set_mode2(self, ser):
        ser.write(bytearray([0, 52, 2]))

    def set_mode3(self, ser):
        ser.write(bytearray([0, 52, 3]))

    def set_mode(self, ser, mode):
        ser.write(bytearray([0, 52, mode]))

    def zero_encoders(self, ser):
        ser.write(bytearray([0, 53]))

    def disable_regulator(self, ser):
        ser.write(bytearray([0, 54]))

    def enable_regulator(self, ser):
        ser.write(bytearray([0, 55]))

    def disable_timeout(self, ser):
        ser.write(bytearray([0, 56]))

    def enable_timeout(self, ser):
        ser.write(bytearray([0, 57]))

    def stop_motors(self, ser):
        ser.flush()
        self.set_speed1(ser, 128)
        self.set_speed2(ser, 128)

    # Moves the motors based on a specified direction.

    def go_dir(self, ser, speed, direction):

        if 45 <= direction < 135:
            self.go_forward(ser, speed)
        elif 135 <= direction < 225:
            self.turn_left(ser, speed)
        elif 225 <= direction < 315:
            self.go_backward(ser, speed)
        else:
            self.turn_right(ser, speed)

    def go_forward(self, ser, speed):
        motor_speed = int(((speed)/100) * 128) + 127
        print(f"Going Forwards... Before: {speed}, After: {motor_speed}")
        self.set_speed1(ser, motor_speed)
        self.set_speed2(ser, motor_speed)

    def go_backward(self, ser, speed):
        motor_speed = int(((100-speed)/100) * 128)
        print(f"Going Backwards... Before: {speed}, After: {motor_speed}")
        self.set_speed1(ser, motor_speed)
        self.set_speed2(ser, motor_speed)

    def turn_right(self, ser, speed):
        forward_speed = int(((speed)/100) * 128) + 127
        backward_speed = int(((100-speed)/100) * 128)
        print(f"Turning Right... Before: {speed}, After: F: {forward_speed}, B: {backward_speed}")
        self.set_speed1(ser, forward_speed)
        self.set_speed2(ser, backward_speed)

    def turn_left(self, ser, speed):
        forward_speed = int(((speed)/100) * 128) + 127
        backward_speed = int(((100-speed)/100) * 128)
        print(f"Turning Left... Before: {speed}, After: F: {forward_speed}, B: {backward_speed}")
        self.set_speed1(ser, backward_speed)
        self.set_speed2(ser, forward_speed)
