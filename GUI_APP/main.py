"""
File: main.py
Author: Bryce Grant
Class: EE491 (ECE Capstone II)
Description: Integration of wrapped GUI with the zoom SDK
Provide live feed from the camera on the robot to allow user to see robot's environment in real time
"""

from gui import MotorControlGUI 



if __name__ == '__main__':
    ngui = MotorControlGUI()
    ngui.start()

    