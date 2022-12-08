# ROBB

## ROBB uses a custom ROS2 package called server_to_motors

## After changes to the code, you must rebuild the package using the following commands

cd ~/ROBB/ROS/ros2_ws/

colcon build --packages-select server_to_motors

. install/setup.bash (necessary for every terminal before launching ROS nodes)

## Launching ROS Nodes

cd ~/ROBB/ROS/ros2_ws/

### Server Control
ros2 run server_to_motors local_server_talker &

### Motor Control
ros2 run server_to_motors motor_control_listener &

### Camera Control
ros2 run server_to_motors camera_control_listener &

### Object Detection (not fully implemented)
ros2 run server_to_motors object_detection_talker &

## Setup UI/Server

cd ~/ROBB/NUC/Web Server/Components

### Launch UI
npm start

## ROS Documentation
https://docs.ros.org/en/foxy/Releases/Release-Humble-Hawksbill.html
