import numpy as np
import cv2
import pyautogui as pag

cap = cv2.VideoCapture(0)
scr = pag.size()
print(scr,scr.width,scr.height)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

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
    cv2.imshow('quantized',quantized)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
