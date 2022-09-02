#!/bin/bash

echo "Starting install..."

#update pi drivers
apt-get update
apt-get full-upgrade

#install vim
apt-get install vim

#Add uv4l drivers to source list
curl https://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
echo "deb https://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main" | sudo tee /etc/apt/sources.list.d/uv4l.list

#install uv4l drivers
sudo apt-get update
sudo apt-get install uv4l uv4l-server

#cleanup
apt-get autoremove

#update pi firmware
rpi-update

echo "Install finished"
echo "Raspberry Pi will now reboot"

reboot
