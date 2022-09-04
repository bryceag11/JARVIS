#!/bin/bash

echo "Starting install..."

cd ~/

#update pi drivers
apt-get update
apt-get full-upgrade

#install vim
apt-get install vim

#install zoom
sudo apt-get install libxcb-xtest0
wget https://zoom.us/client/5.11.10.4400/zoom_x86_64.tar.xz
tar xvf zoom_x86_64.tar.xz
rm zoom_x86_64.tar.xz

#install box86
apt install git build-essential cmake
git clone https://github.com/ptitSeb/box86
cd ~/box86
mkdir build
cd build
cmake .. -DRPI4=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j$(nproc)
make install
systemctl restart systemd-binfmt

echo "Install finished"
echo "Raspberry Pi will now reboot"

reboot
