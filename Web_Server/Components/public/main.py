
from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


# Main landing page
@app.route("/")
def nav():
    return render_template("nav.html")

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
def index():
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
