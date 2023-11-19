"""
File Name: main_gui.py

Description: Executable GUI script

Usage: Make sure to have the necessary dependencies installed.
       Reference the motor_control usage

Author: Bryce Grant

Class: EE491 (ECE Capstone II)
"""

from gui_wrapper import MotorControlGUI 



if __name__ == '__main__':
    ngui = MotorControlGUI()
    ngui.start()

    