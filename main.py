from flask import Flask, render_template, request
import serial
import serial.tools.list_ports
import time

app = Flask(__name__)

# Establish serial connection with ardunio
# arduino = serial.Serial('/dev/ttyUSB0', 9600) #Update path to correct ardunio port on NUC
# time.sleep(2)

# def packet_reader(ser):
#     while True:
#         if ser.in_waiting:
#             packet = ser.readline()
#             print(packet.decode('utf')) 

##app.config["SECRET_KEY"] = "testkey"

# Main landing page
@app.route("/")
def index():
    return render_template("nav.html")

# # Camera Control
# @app.route('/control', methods=['POST'])
# def control():
#     command = request.form['command'] #Get command from webpage input
#     arduino.write(command.encode()) #Send command to arduino
#     response_message = 'Command sent to Arduino: ' + command
#     return render_template('cdn.html', response=response_message)

# @app.route("/cdn")
# def cdn():
#     return render_template("cdn.html")

# #list available serial ports
# ports = serial.tools.list_ports.comports()
# #Open serial port
# ser=serial.Serial()
# portList = []

# for onePort in ports:
#     portList.append(str(onePort))
#     print(str(onePort))

# val = input("select Port: COM")

# porVar = None #initialize

# for x in range(0,len(portList)):
#     if portList[x].startswith("COM" + str(val)):
#         portVar = "COM" + str(val)
#         print(portList[x])

# if portVar:
#     ser.baudrate = 9600
#     ser.port = portVar
#     ser.open()

#     packet_reader(ser)

# else:
#     print("Invalid port selection.")   

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
    
