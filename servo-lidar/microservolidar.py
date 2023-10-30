#https://github.com/lakshmanmallidi/PyLidar3

import PyLidar3
import cv2
import numpy as np
import math as m,math
import time # Time module
import serial

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=.025)
print("//waiting for Serial connection...")
time.sleep(0.5)

def write_read(x):

    arduino.write(bytes(str(x), 'utf-8'))
    #arduino.write( str(x).encode() )
    time.sleep(0.025)
    data = arduino.readline()
    return data

def Rx(theta):
  return np.array([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
 
def Ry(theta):
  return np.array([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])
 
def Rz(theta):
  return np.array([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

def printxyz(v):
    print(v[0],v[1],v[2])
            

chunk_size = 512*4 
upos_start = 1500
upos = upos_start
upos_end = 2000
upos_incr = 6 
upos_ratio_correction = 3.33
vers = 1
wait_ms = 100  #56 # 33 

#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
port = "/dev/ttyUSB0" #linux
#port = "/dev/ttyACM0"  #linux

Obj = PyLidar3.YdLidarX4(port,chunk_size) #PyLidar3.your_version_of_lidar(port,chunk_size) 
if(Obj.Connect()):
    print("/*",Obj.GetDeviceInfo(),"*/")
    print(f"// chunk_size={chunk_size}")
    print(f"// wait_ms={wait_ms}")
    print(f"// upos_start={upos}")
    print(f"// upos_end={upos_end}")
    print(f"// upos_incr={upos_incr}")
    print(f"// upos_ratio_correction = {upos_ratio_correction}") 

    #print(dir(Obj))

    gen = Obj.StartScanning()
    t = time.time() # start time 

    #im = np.ndarray( (900,1440,3),dtype="uint8")
    im = np.ndarray( (320,900,3),dtype="uint8")
    cim = im.copy()
    zoom = 1 

    #while (time.time() - t) < 30: #scan for 30 seconds

    #print("//w=2;")#openscad cube width
    #print("//color(\"aqua\")rotate([-90,0,0]){")

    #MOVE MICRO SERVO TO START POSITION
    bpos = write_read(upos)    
    time.sleep(1)

    while True:

        #Move Micro Servo
        bpos = write_read(upos)
        ipos = bpos.decode()
        
        #print(bpos,ipos) # printing the value
        #time.sleep(0.050)

        #GET LIDAR DATA 
        data=next(gen)
        #print(data)
        #print(">")
       
        im=cim.copy()

        center = (0,int(im.shape[0]/2)) 
        lcnt=[center]

        #Transform Lidar data

        for deg in range(0,360,1):
            dist = data[deg]
            rdeg=deg+180
            
            x= 0 + math.sin(math.radians(rdeg)) * dist * zoom
            y= im.shape[0]/2 + math.cos(math.radians(rdeg)) * dist * zoom

            x3d = np.round(math.sin(math.radians(rdeg)) * dist,decimals=2) 
            y3d = np.round(math.cos(math.radians(rdeg)) * dist,decimals=2)
            z3d = 4.5

            #PRINT POINTS 
            #print(pos, rdeg, dist, end=", ")
            #print( pos, x3d , y3d,0)

            pos = np.round(360/1000 * (upos-1000) / upos_ratio_correction,decimals=2)
            #print(f"rotate([0,{pos},0])translate([{x3d},{y3d},{z3d}])cube(w,true);")
            
            #ROTATE POINT IN Y 
            v1 = np.array([x3d,y3d,z3d])
            #rv1 = v1 * Ry(math.radians(pos))     
            rv1y = Ry(math.radians(pos))
                    
            rv1= [np.sum(rv1y[0]*v1), 
                    np.sum(rv1y[1]*v1),
                    np.sum(rv1y[2]*v1)] 
            
            printxyz( np.round(rv1,decimals=2) )

            #Cono Campo visivo webcam
            kdeg = 434  #180 - 539 
            if dist > 0 and rdeg >= kdeg and rdeg <= kdeg+32 : 
                lcnt.append([x,y]) #avoiding noise
                cv2.circle(im, (int(x),int(y)), 2 , (0,0,255),-1)  #Point

        #print("---")

        ctr = np.array(lcnt).reshape((-1,1,2)).astype(np.int32)
        cv2.drawContours(im,[ctr],0,(0,255,0),-1)


        #cross
        
        #xf1=int( im.shape[1]/2 +  math.cos(math.radians(16)) * 10000 * zoom)
        xf1 = int( 0 +  math.cos(math.radians(16)) * 10000 * zoom)
        yf1 = int( im.shape[0]/2 +  math.sin(math.radians(16)) * 10000 * zoom)
        #xf2= int( im.shape[1]/2 +  math.cos(math.radians(-16)) * 10000 * zoom)
        xf2 = int( 0 +  math.cos(math.radians(-16)) * 10000 * zoom)
        yf2 = int( im.shape[0]/2 +  math.sin(math.radians(-16)) * 10000 * zoom)
   
        im = cv2.line(im,center,(xf1,yf1),(0,0,255),1)
        im = cv2.line(im,center,(int(im.shape[1]), int(im.shape[0]/2)),(0,0,255),1)
        im = cv2.line(im,center,(xf2,yf2),(0,0,255),1)



        #The Lidar
        cv2.circle(im, center, int(30*zoom) , (255,0,0),-1)
        #The workspace 
        cv2.circle(im, center, int(300*zoom) , (0,0,255),3)
        #for mm in range(0,2000,100):
        #    thickness = 2 if mm % 1000 == 0 else 1
        #    cv2.circle(im, center, int(mm*zoom) , (255,0,0),thickness)

        #cv2.imshow("Lidar",cv2.flip(im,-1))
        cv2.imshow("Lidar",im)

        #INCREMENT SERVO POSITION
        '''
        pos += vers        
        if pos < 1 or pos >= 180: 
            vers *= -1 
            print("}")#END OPENSCAD 
            break
        '''

        #INCREMENT SERVO MICRO POSITION
        upos += (upos_incr * vers)
        #if upos < 1000 or upos >= 2000: 
        if upos < upos_start or upos >= upos_end:
            vers *= -1 
            print("//}")#END OPENSCAD 
            break


        k = cv2.waitKey(wait_ms)
        #k = cv2.waitKey(33)
        if k==ord("q"):break
        if k==ord("z"):zoom-=0.05
        if k==ord("x"):zoom+=0.05

        #time.sleep(0.5)
        #time.sleep(0.33)

    Obj.StopScanning()
    Obj.Disconnect()
    cv2.destroyAllWindows()

else:
    print("Error connecting to device")

