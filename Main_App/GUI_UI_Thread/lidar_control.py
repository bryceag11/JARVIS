"""
File Name: lidar_control.py

Description: This script creates a class for the vis

Usage: Make sure to have the necessary dependencies installed, and provide correct 
       port information for both the motors and the LiDAR device.

Author: Bryce Grant

Class: EE491 (ECE Capstone II)
"""

import PyLidar3
import cv2
import numpy as np
import math 
import time # Time module
import serial
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *