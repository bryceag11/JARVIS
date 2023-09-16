
import tkinter as tk
from tkinter import ttk
from motor_commands import MotorCommands
from camera_control import CameraControl

class MotorControlGUI:
    def __init__(self, port="COM3"):
        self.root = tk.Tk() #initialize tkinter
        self.root.title("Motor Control")
        self.motor_commands = MotorCommands() #create instance of the commands
        self.camera_control = CameraControl() #create instance of camera commands
        self.port = port
        self.ser = None
        self.motor_speed = 50
        self.create_widgets()

    def create_widgets(self):
        # ttk.Label(self.root, text="Enter Port:").grid(row=0, column=0)
        # self.port_entry = ttk.Entry(self.root)
        # self.port_entry.insert(0, "COM3")  
        # self.port_entry.grid(row=0, column=1)
        ttk.Button(self.root, text="Connect and Initialize", command=self.connect_and_initialize).grid(row=0, column=1)

        #motor buttons
        ttk.Button(self.root, text="Forward", command=lambda: self.motor_button_drive("forward")).grid(row=1, column=1)
        ttk.Button(self.root, text="Backward", command=lambda: self.motor_button_drive("backward")).grid(row=3, column=1)
        ttk.Button(self.root, text="Left", command=lambda: self.motor_button_drive("left")).grid(row=2, column=0)
        ttk.Button(self.root, text="Right", command=lambda: self.motor_button_drive("right")).grid(row=2, column=2)
        ttk.Button(self.root, text="Stop", command=lambda: self.motor_button_drive("stop")).grid(row=2, column=1)
        ttk.Button(self.root, text="RotateL", command=lambda: self.motor_button_drive("rotate_left")).grid(row=1, column=0)
        ttk.Button(self.root, text="RotateR", command=lambda: self.motor_button_drive("rotate_right")).grid(row=1, column=2)

        self.root.bind('<Up>', lambda event: self.motor_button_drive("forward"))
        self.root.bind('<Down>', lambda event: self.motor_button_drive("backward"))
        self.root.bind('<Left>', lambda event: self.motor_button_drive("left"))
        self.root.bind('<Right>', lambda event: self.motor_button_drive("right"))
        self.root.bind('<space>', lambda event: self.motor_button_drive("stop"))
        self.root.bind('<a>', lambda event: self.motor_button_drive("rotate_left"))
        self.root.bind('<d>', lambda event: self.motor_button_drive("rotate_right"))

        #camera buttons
        ttk.Button(self.root, text="Up", command=lambda: self.camera_button_drive("up")).grid(row=5, column=0)
        ttk.Button(self.root, text="Down", command=lambda: self.camera_button_drive("down")).grid(row=5, column=1)
        ttk.Button(self.root, text="Left", command=lambda: self.camera_button_drive("left")).grid(row=5, column=2)
        ttk.Button(self.root, text="Right", command=lambda: self.camera_button_drive("right")).grid(row=5, column=3)

        ttk.Label(self.root, text="Speed:").grid(row=4, column=0)
        self.speed_slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_speed)
        self.speed_slider.set(self.motor_speed)  # Set default speed to 50
        self.speed_slider.grid(row=4, column=1, columnspan=2)

    def motor_button_drive(self, action):
        if self.ser is not None:
            if action == "forward":
                self.motor_commands.go_forward(self.ser, self.motor_speed)
            elif action == "backward":
                self.motor_commands.go_backward(self.ser, self.motor_speed)
            elif action == "left":
                self.motor_commands.turn_left(self.ser, self.motor_speed)
            elif action == "right":
                self.motor_commands.turn_right(self.ser, self.motor_speed)
            elif action == "stop":
                self.motor_commands.stop_now(self.ser)
            elif action == "rotate_left":
                self.motor_commands.turn_left(self.ser, 25)
            elif action == "rotate_right":
                self.motor_commands.turn_right(self.ser, 25)

    def camera_button_drive(self, action):
        if action == "up":
            self.camera_control.go_up()
        elif action == "down":
            self.camera_control.go_down()
        elif action == "left":
            self.camera_control.go_left()
        elif action == "right":
            self.camera_control.go_right()

    def update_speed(self, val):
        self.motor_speed = round(float(val))
        self.update_motor_speed()

    def update_motor_speed(self):
        if self.ser is not None:
            motor_speed = int(((100-self.motor_speed)/100) * 127) 
            self.motor_commands.set_speed1(self.ser, motor_speed)
            self.motor_commands.set_speed2(self.ser, motor_speed)

    def connect_and_initialize(self):
        self.ser = self.motor_commands.connect_motors(self.port)
        self.motor_commands.initialize_motors(self.ser)
    def start(self):
        self.root.mainloop()
