#!/bin/bash

FILE="$HOME/.ssh/selfsign.key"
DEVICE_ID="046d:0825"
DEVICE_NAME="video0"
WIDTH="1920"
HEIGHT="1080"

#gen keys if they do not exist
if [ ! -d "$HOME/.ssh" ]; then
	echo "Adding .ssh director to $HOME"
	mkdir "$HOME/.ssh"
fi
if [ ! -f "$FILE" ]; then
	echo "Generating ssh key into $HOME/.ssh/"
	openssl genrsa -out selfsign.key 2048 && openssl req -new -x509 -key selfsign.key -out selfsign.crt -sha256
	mv selfsign* .ssh/
fi	

#stop current uv4l services
#sudo service uv4l* stop

#set camera resolution
v4l2-ctl --set-fmt-video=width=$WIDTH,height=$HEIGHT -d /dev/video0

#set camera format
#TODO not working
#v412-ctl --set-fmt-video=width=$WIDTH,height=$HEIGHT,pixelformat="MPJEG" -d /dev/video0


#run streaming server in background
OPTIONS="\
--syslog-host localhost \
--external-driver \
--device-name $DEVICE_NAME \
--device-id $DEVICE_ID \
--driver-name $DEVICE_NAME \
--verbosity 8 \
--server-option --use-ssl=yes \
--server-option --ssl-private-key-file=$HOME/.ssh/selfsign.key \
--server-option --ssl-certificate-file=$HOME/.ssh/selfsign.crt \
"

uv4l $OPTIONS
