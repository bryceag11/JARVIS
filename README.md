# J.A.R.V.I.S. (Just a rather very intelligent system)

## J.A.R.V.I.S. is a social navigating robot that aspires to provide an immersive, autonomous experience for its remote users

# Features
* Autonomous navigation using a [YDLidar X4](https://github.com/YDLIDAR/YDLidar-SDK)
* Web integration with Zoom for remote user control and interaction
* Manual and autonomous motor control
* Camera control for user interaction

## Getting Started
### Clone the project repository
git clone https://github.com/bryceag11/JARVIS.git

cd JARVIS

### Install the dependencies
pip install -r requirements.txt

## GUI Usage
### Launch the main program
python Main_App/GUI_UI_Thread/main.py

## Lidar Usage
### 3D Point Cloud Production
python Main_App/Lidar_Thread/lidar_servo_slam.py

### Point Cloud Viewer
python Main_App/Lidar_Thread/opengl_viewer.py

## Autonomous Robotic Movement
python Main_App/Lidar_Thread/rover_lidar.py


## Setup UI/Server

cd ~/JARVIS/NUC/Web Server/Components

### Launch Zoom UI
npm start


## Please refer to our Final Report for further information on the robot
