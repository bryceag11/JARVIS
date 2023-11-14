import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

#Open serial port
ser=serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

ser.baudrate = 9600
ser.port = portVar
ser.open()

while True:
    if ser.in_waiting:
        packet = ser.readline()
        print(packet.decode('utf'))
        