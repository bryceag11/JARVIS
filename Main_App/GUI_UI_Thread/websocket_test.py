import netifaces as ni 

nucIP = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
print("NUC IP is: " + nucIP)
