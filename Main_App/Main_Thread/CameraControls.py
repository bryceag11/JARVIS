import serial

class Camera_Control:
    def __init__(self, arduino_port='/dev/ttyACM0'):
        self.arduino_port = arduino_port

    def connect_to_arduino(self, port):
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = port
        ser.open()

        if ser.is_open:
            print(f"Successfully connected to Arduino on port {self.arduino_port}\n")
            return ser
        else:
            print(f"Failed to connect to Arduino on port {self.arduino_port}\n")
            return None

    def move_left(self, serie):
        serie.write(b'a')

    def move_right(self, serie):
        serie.write(b'd')

    def move_up(self, serie):
        serie.write(b'w')

    def move_down(self, serie):
        serie.write(b's')

    def change_mode(self, serie):
        serie.write(b'm')

    # add if neededd
    #def stop_motors(self):
        # Send a stop signal or any other command as needed to stop motors
        # pass

    def close_connection(self, serie):
        if serie.is_open:
            serie.close()
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
