#!/bin/bash

echo "Starting Install/Setup..."

sudo apt update
sudo apt full-upgrade -y

#install vim
sudo apt install -y vim

#install/enable ssh
sudo apt install -y openssh
sudo ufw allow ssh

#install ROS2
echo "\nInstalling ROS2 packages..."
apt-cache policy | grep universe
sudo apt update
sudo apt install curl gnupg lsb-release -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade -y
sudo apt install -y ros-humble-desktop

echo "Install/Setup Finished"