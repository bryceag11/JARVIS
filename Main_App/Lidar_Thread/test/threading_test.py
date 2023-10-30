from Main_App.GUI_UI_Thread.motor_control import MotorCommands
import threading
import PyLidar3
import math
import time

motor = MotorCommands()
ser = motor.connect_motors("dev/ttyUSB0")
motor.initialize_motors(ser)

speed = 25
direction = 0.0 # direction in degrees

def drive():
    while True:
        motor.go_dir(ser, speed, direction)


x=[]
y=[]
for _ in range(360):
    x.append(0)
    y.append(0)

port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarX4(port)  #PyLidar3.your_version_of_lidar(port,chunk_size)
threading.Thread(target=drive).start()
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time
    while (time.time() - t) < 10: #scan for 30 seconds
        data = next(gen)
        print("got new data")
        for angle in range(0,360):
            if(data[angle]>1000):
                x[angle] = data[angle] * math.cos(math.radians(angle))
                y[angle] = data[angle] * math.sin(math.radians(angle))
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
