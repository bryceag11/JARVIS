import PyLidar3
import time 

# serial port to which lidar connected
# in linux type in terminal -- ls /dev/tty*'
port = "/dev/ttyUSB0" # linux
Obj = PyLidar3.YdLidarX4(port) # PyLidar3.YdLidarX4(port,chunk_size)

if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # Start time

    while (time.time() - t) < 30: # Scan for 30 seconds
        next(gen)
        print(time.time())
    Obj.StopScanning()
    Obj.Disconnect()
    
else:
    print("Error connecting to device")
