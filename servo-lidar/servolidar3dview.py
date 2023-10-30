#https://github.com/lakshmanmallidi/PyLidar3
#~/.local/lib/python3.6/site-packages/PyLidar3/__init__.py  is the library with some modification  

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

pos=0
vers=1
v3dr=180
pos_init= 0
pos_end = 32
pos_step=2
lidar_chunk_size=1280*2
#lidar_chunk_size=200
dist_limit=2000

#VIDEOCAPTURE
cap = cv2.VideoCapture(0)

def videocam(frame):

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #rfr = cv2.resize(frame,(640,480))
    #rfr = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rfr = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow('frame',rgray)

    # colorReduce()
    div = 64 
    quantized = (rfr // div * div) + div // 2
    # ksize
    ksize = (10, 10) 
    # Using cv2.blur() method 
    quantized = cv2.blur(quantized, ksize) 



    cv2.line( rfr,
            (0,int(rfr.shape[0]/2)),
            (int(rfr.shape[1]), int(rfr.shape[0]/2)),
            (0, 255, 0), 1)

    cv2.line( rfr,
            (int(rfr.shape[1]/2),0),
            (int(rfr.shape[1]/2), int(rfr.shape[0])),
            (0, 255, 0), 1)

    cv2.imshow('frame',rfr)
    #cv2.imshow('quantized',quantized)

    return rfr   



def Render(pts):

    #https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawArrays.xhtml
    glPointSize(2)
    glBegin(GL_POINTS)  
    sc=0.001
    fk = 180-len(pts)

    for i in range(0,len(pts)):

        p = ( 
            sc*pts[i][0],
            sc*pts[i][1],
            sc*pts[i][2] 
            )
    
        maxlength=1000
        r=cmap(pts[i][2],0,maxlength,0,1)
        g=cmap(pts[i][1],0,maxlength,0,1)
        b=cmap(pts[i][0],0,maxlength,0,1)
        
        glColor3f(b,g,r) 
        glVertex3fv(p)

    '''
    for i in range(0, fk ):
        p=(0,0,0)
        r,g,b = 0,0,0

        glColor3f(b,g,r) 
        glVertex3fv(p)
    '''

    glEnd()



def cmap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / float(in_max - in_min) + out_min;


def Rx(theta):
  return np.array([[ 1, 0           , 0           ],
                   [ 0, math.cos(theta),-math.sin(theta)],
                   [ 0, math.sin(theta), math.cos(theta)]])
 
def Ry(theta):
  return np.array([[ math.cos(theta), 0, math.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-math.sin(theta), 0, math.cos(theta)]])
 
def Rz(theta):
  return np.array([[ math.cos(theta), -math.sin(theta), 0 ],
                   [ math.sin(theta), math.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])


def write_read(x):

    arduino.write(bytes(str(x), 'utf-8'))
    #arduino.write( str(x).encode() )
    time.sleep(0.05)
    data = arduino.readline()
    return data


arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=.015)
print("//waiting for Serial connection...")
time.sleep(0.5)

#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
port = "/dev/ttyUSB0" #linux
#port = "/dev/ttyACM0"  #linux
Obj = PyLidar3.YdLidarX4(port, lidar_chunk_size) #PyLidar3.your_version_of_lidar(port,chunk_size)
points=[]
lpoints=[]

if(Obj.Connect()):
    print("/*",Obj.GetDeviceInfo(),"*/")

    gen = Obj.StartScanning()
    t = time.time() # start time 

    im = np.ndarray( (320,900,3),dtype="uint8")
    cim = im.copy()
    zoom = 1 

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
                                                                                                                                                                                                                            

    while True:


        #Move Servo
        bpos = write_read(pos)
        ipos = bpos.decode()
        print(pos,ipos)

        #print(pos,ipos)
        #GET LIDAR DATA 
        data=next(gen)
        
        im=cim.copy()

        center = (0,int(im.shape[0]/2)) 
        lcnt   = [center]

        #Transform Lidar data

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret: frm = videocam(frame)

        for deg in range(0,360,1):

            dist = data[deg]
           
            if dist > dist_limit:continue

            rdeg=deg+180
            #print(data)

            x = 0 + math.sin(math.radians(rdeg)) * dist * zoom
            y = im.shape[0]/2 + math.cos(math.radians(rdeg)) * dist * zoom

            x3d = math.sin(math.radians(rdeg)) * dist 
            y3d = math.cos(math.radians(rdeg)) * dist 
            z3d = 4.5
     
            #ROTATE POINT IN Y 
            v1 = np.array([x3d,y3d,z3d])
            rv1y = Ry(math.radians(pos))
            

            #print(frm[0][0])



            rv1= [np.sum(rv1y[0]*v1), 
                  np.sum(rv1y[1]*v1),
                  np.sum(rv1y[2]*v1)] 



            zr=rv1[2];
            yr=rv1[1];

            rpp = [-50,yr,0]; #rayprojpoint
            mrpp=rpp[1]/rpp[0];
            ix2=200/mrpp;
            
            try: 

                mzpp=yr/zr;
                iz=200/mzpp;

                resx=int(ix2)   #, 200 , iz
                resy=int(200)
                resz=int(iz)

                print(resx,resy,resz)
                #r,g,b=frm[resx][resz]           
                #print(r,g,b)

            except:                
                print("except mzpp inf")


            points.append(rv1)

            #Cono Campo visivo webcam
            kdeg = 434  #180 - 539 
            if dist > 0 and rdeg >= kdeg and rdeg <= kdeg+32 : 
                lcnt.append([x,y]) #avoiding noise
                cv2.circle(im, (int(x),int(y)), 2 , (0,0,255),-1)  #Point

        #print("---")

        ctr = np.array(lcnt).reshape((-1,1,2)).astype(np.int32)
        cv2.drawContours(im,[ctr],0,(0,255,0),-1)

        #OPENGL VIEWER

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keypress = pygame.key.get_pressed()#Move using WASDZY
        if keypress[pygame.K_w]:
            glTranslatef(0,0,0.1)
        if keypress[pygame.K_s]:
            glTranslatef(0,0,-0.1)
        if keypress[pygame.K_d]:
            glTranslatef(-0.1,0,0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1,0,0)
        if keypress[pygame.K_z]:
            glTranslatef(0,-0.1,0)
        if keypress[pygame.K_x]:
            glTranslatef(0,0.1,0)


        if keypress[pygame.K_r]:
            glRotatef(-5.,0.,1.,0.)
        if keypress[pygame.K_t]:
            glRotatef(5.,0.,1.,0.)


        glPushMatrix()
        glTranslate(0,-1,1)
        glRotatef(180, 1, 0, 0)
        glRotatef(v3dr, 0, 1, 0)

        glClearColor(0.5, 0.5, 0.5, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Render(lpoints)
        Render(points)
        pygame.display.flip()
        #pygame.time.wait(10)
        glPopMatrix()



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

        cv2.imshow("Lidar",cv2.flip(im,0))
        #cv2.imshow("Lidar",cv2.flip(im,1))
        #cv2.imshow("Lidar",cv2.flip(im,-1))

        #LIDAR SHOW
        #cv2.imshow("Lidar",im)

        #INCREMENT SERVO POSITION
        '''
        ok
        pos += vers        
        if pos < 1 or pos >= 180: 
            vers *= -1 
            #print("}")#END OPENSCAD 
            #break
        '''

        pos += pos_step*vers        
        if pos <= pos_init or pos >= pos_end:
            vers *= -1
            lpoints = points.copy()
            points=[]
            #break

        if pos < pos_init: pos=pos_init+pos_step
        if pos > pos_end: pos = pos_end-pos_step

        k = cv2.waitKey(1)
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

