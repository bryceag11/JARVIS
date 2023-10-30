import tkinter as tk
from tkinter import ttk
from motor_commands import MotorCommands
from camera_control import CameraControl

class MotorControlGUI:
    def __init__(self, port="/dev/ttyUSB0"):
        self.root = tk.Tk()  # Initialize tkinter
        self.root.title("J.A.R.V.I.S. Control")
        self.root.geometry("650x300")  # Set a fixed size (adjust dimensions as needed)
        self.root.configure(bg="black")  # Set the overall background to black
        self.root.resizable(width=False, height=False)  # Make the window non-resizable

        self.motor_commands = MotorCommands()
        # self.camera_control = CameraControl()

        self.port = port
        self.ser = None
        self.motor_speed = 50

        self.create_widgets()
        self.setup_key_bindings()

    def create_widgets(self):
        # Frame for motor controls
        motor_frame = ttk.Frame(self.root, padding=(10, 10), relief="groove", borderwidth=2)
        motor_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        motor_frame.configure(style='Maroon.TFrame')

        # Title for motor controls
        ttk.Label(motor_frame, text="Motor Controls", font=("Tahoma", 16, "bold"), background="Gold", foreground="Maroon").grid(row=0, columnspan=3, pady=(10, 5))

        # Motor buttons (gaming controller-like layout)
        ttk.Button(motor_frame, text="⮙", command=lambda: self.motor_button_drive("forward"), style="Controller.TButton").grid(row=1, column=1)
        ttk.Button(motor_frame, text="⮛", command=lambda: self.motor_button_drive("backward"), style="Controller.TButton").grid(row=3, column=1)
        ttk.Button(motor_frame, text="⮚", command=lambda: self.motor_button_drive("right"), style="Controller.TButton").grid(row=2, column=2)
        ttk.Button(motor_frame, text="⮘", command=lambda: self.motor_button_drive("left"), style="Controller.TButton").grid(row=2, column=0)
        ttk.Button(motor_frame, text="■", command=lambda: self.motor_button_drive("stop"), style="Controller.TButton").grid(row=2, column=1)
        ttk.Button(motor_frame, text="⟲", command=lambda: self.motor_button_drive("rotate_left"), style="Controller.TButton").grid(row=1, column=0)
        ttk.Button(motor_frame, text="⟳", command=lambda: self.motor_button_drive("rotate_right"), style="Controller.TButton").grid(row=1, column=2)

        # Slider for motor speed
        self.speed_slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_speed)
        self.speed_slider.set(self.motor_speed)  # Set default speed to 50
        self.speed_slider.grid(row=5, column=0, columnspan=3, pady=(10, 20))

        # Frame for camera controls
        camera_frame = ttk.Frame(self.root, padding=(10, 10), relief="groove", borderwidth=2)
        camera_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        camera_frame.configure(style='Maroon.TFrame')

        # Title for camera controls
        ttk.Label(camera_frame, text="Camera Controls", font=("Tahoma", 16, "bold"), background="Gold", foreground="Maroon").grid(row=0, columnspan=4, pady=(10, 5))

        # Camera buttons
        ttk.Button(camera_frame, text="⮙", command=lambda: self.camera_button_drive("up"), style="Camera.TButton").grid(row=1, column=1)
        ttk.Button(camera_frame, text="⮛", command=lambda: self.camera_button_drive("down"), style="Camera.TButton").grid(row=3, column=1)
        ttk.Button(camera_frame, text="⮚", command=lambda: self.camera_button_drive("right"), style="Camera.TButton").grid(row=2, column=2)
        ttk.Button(camera_frame, text="⮘", command=lambda: self.camera_button_drive("left"), style="Camera.TButton").grid(row=2, column=0)

        # Configure weights for frames and columns to allow resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Define custom styles for buttons and slider
        ttk.Style().configure("Controller.TButton", font=("Arial", 12), background="Gold", foreground="Maroon", width=10)
        ttk.Style().configure("Horizontal.TScale", sliderlength=30, troughcolor="Gold", background="Maroon")

        # Define custom styles for frames
        ttk.Style().configure("Maroon.TFrame", background="maroon")
        ttk.Style().configure("Gold.TFrame", background="gold")
        ttk.Style().configure("Camera.TButton", font=("Modern", 12), background="gold", foreground="maroon", width=10)

    def setup_key_bindings(self):
        self.root.bind('<Up>', lambda event: self.motor_button_drive("forward"))
        self.root.bind('<Down>', lambda event: self.motor_button_drive("backward"))
        self.root.bind('<Left>', lambda event: self.motor_button_drive("left"))
        self.root.bind('<Right>', lambda event: self.motor_button_drive("right"))
        self.root.bind('<space>', lambda event: self.motor_button_drive("stop"))
        self.root.bind('<a>', lambda event: self.motor_button_drive("rotate_left"))
        self.root.bind('<d>', lambda event: self.motor_button_drive("rotate_right"))

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
            motor_speed = int(((100 - self.motor_speed) / 100) * 127)
            self.motor_commands.set_speed1(self.ser, motor_speed)
            self.motor_commands.set_speed2(self.ser, motor_speed)

    def connect_and_initialize(self):
        self.ser = self.motor_commands.connect_motors(self.port)
        self.motor_commands.initialize_motors(self.ser)

    def start(self):
        self.connect_and_initialize()
        self.root.mainloop()

