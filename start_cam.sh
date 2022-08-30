#!/bin/bash

FILE="$HOME/.ssh/selfsign.key"
DEVICE_ID="046d:0825"


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
sudo service uv4l* stop

#run streaming server
exec sudo uv4l --syslog-host localhost --driver uvc --device-id $DEVICE_ID -n video0 /dev/uv4l --verbosity 8 -f --server-option --use-ssl=yes --server-option --ssl-private-key-file=$HOME/.ssh/selfsign.key --server-option --ssl-certificate-file=$HOME/.ssh/selfsign.crt --server-option --enable-webrtc=yes --server-option --enable-webrtc-video=yes
