# J.A.R.V.I.S.
# Or, Just a rather very intelligent sysem

## J.A.R.V.I.S. uses a custom ROS2 package called server_to_motors

## After changes to the code, you must rebuild the package using the following commands

cd ~/ROBB/ROS/ros2_ws/

colcon build --packages-select server_to_motors

. install/setup.bash (necessary for every terminal before launching ROS nodes)

## Launching ROS Nodes (scripts located in /ROS/ros2_ws/src/server_to_motors/server_to_motors)

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

## VL53L1X I2C Examples (ToF sensors)
https://www.l33t.uk/ebay/vl53l1x/

## Please refer to our Final Report for further information on the robot
