import serial

class CameraControls:
    def __init__(self, arduino_port='/dev/ttyUSB0'):
        self.arduino_port = arduino_port
        self.ser = self.connect_to_arduino()

    def connect_to_arduino(self):
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = self.arduino_port
        ser.open()

        if ser.is_open:
            print(f"Successfully connected to Arduino on port {self.arduino_port}\n")
            return ser
        else:
            print(f"Failed to connect to Arduino on port {self.arduino_port}\n")
            return None

    def move_left(self):
        self.ser.write(b'a')

    def move_right(self):
        self.ser.write(b'd')

    def move_up(self):
        self.ser.write(b'w')

    def move_down(self):
        self.ser.write(b's')

    def change_mode(self):
        self.ser.write(b'm')

    # add if neededd
    #def stop_motors(self):
        # Send a stop signal or any other command as needed to stop motors
        # pass

    def close_connection(self):
        if self.ser.is_open:
            self.ser.close()
            print("Connection closed\n")
        else:
            print("Connection is not open\n")

# Example usage:
# camera_controls = CameraControls()
# camera_controls.move_left()
# camera_controls.move_up()
# camera_controls.change_mode()
# camera_controls.stop_motors()
# camera_controls.close_connection()