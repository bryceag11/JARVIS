"""
File: main.py
Author: Bryce Grant
Class: EE491 (ECE Capstone II)
Description: Integration of wrapped GUI with the zoom SDK
Provide live feed from the camera on the robot to allow user to see robot's environment in real time
"""

import webview
from gui import start_gui



if __name__ == '__main__':

    webview.create_window("J.A.R.V.I.S. Control", html="<p>Placeholder for embedded GUI</p>", js_api=start_gui)
    webview.start()
    