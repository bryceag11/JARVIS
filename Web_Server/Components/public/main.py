'''


from flask import Flask, render_template, request
from flask_socketio import SocketIO
import serial
import time

app = Flask(__name__,  static_folder='/static')
SocketIO=SocketIO(app)

# Establish serial connection with ardunio
# arduino = serial.Serial('/dev/ttyUSB0', 9600) #Update path to camera ardunio port on NUC
# time.sleep(2)

##app.config["SECRET_KEY"] = "testkey"

# Main landing page
@app.route("/")
def index():
    return render_template("nav.html")

# All necessary routes
@app.route("/static/jsrsasign-all-min.js")
@app.route("/static/tool.js")
@app.route("/static/token-tool.js")
@app.route("/static/vconsole.min.js")
@app.route("/static/nav.js")
@app.route("/static/static/tool.js")
@app.route("/static/static/vconsole.min.js")
@app.route("/static/static/token-tool.js")
@app.route("/static/static/cdn.js")
@app.route("/static/teamlogo.png")
@app.route("/static/cdn.js")
@app.route("/cdn.css")
@app.route("/static/cdn.css")

# WebSocket Handling
@SocketIO.on('connect')
def handle_connect():
    print("Client Connected Successfully")
   

@SocketIO.on('disconnect')
def handle_disconenct():
    print("Client Disconnected")

# # # Camera Control
# @app.route('/control', methods=['POST'])
# def control():
#     command = request.form['command'] #Get command from webpage input
#     arduino.write(command.encode()) #Send command to arduino
#     response_message = 'Command sent to Arduino: ' + command
#     return render_template('cdn.html', response=response_message)

@app.route("/cdn")
def cdn():
    return render_template("cdn.html")


if __name__ == "__main__":
    SocketIO.run(app, debug=True, port=5000, host='0.0.0.0')
'''

from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


# Main landing page
@app.route("/")
def index():
    return render_template("nav.html")

# @app.route("/cdn.html")
# def cdn():
#     return render_template("cdn.html")

@app.route("/cdn.html", methods=['GET', 'POST'])
def cdn():
    if request.method == 'POST':
        command = request.form['command'] # Get command from webpage input
        # Perform action with Arduino or other necessary logic here
        
        # For instance, assuming you have arduino available
        # arduino.write(command.encode())
        
        response_message = 'Command sent to Arduino: ' + command
        return render_template('cdn.html', response=response_message)
    
    # Render the cdn.html template for GET requests
    return render_template("cdn.html")


@app.route("/index")
def nav():
    return render_template("index.html")

# # # Camera Control
# @app.route('/control', methods=['POST'])
# def control():
#     command = request.form['command'] #Get command from webpage input
#     arduino.write(command.encode()) #Send command to arduino
#     response_message = 'Command sent to Arduino: ' + command
#     return render_template('cdn.html', response=response_message)

# WebSocket Handling
@socketio.on('connect')
def handle_connect():
    print("Client Connected Successfully")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client Disconnected")

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0")

