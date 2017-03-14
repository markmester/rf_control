#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


echo "Installing dependencies..."
echo "##########################"
apt update
apt install python3-pip supervisor unzip -y
pip install pyaml flask flask-ast
pip3 install rpi-rf

echo "Unpacking ngrok..."
echo "##################"
unzip ngrok-stable-linux-arm.zip
rm -rf ngrok-stable-linux-arm.zip

echo "Creating logs..."
echo "##################"
mkdir /var/log/rf
touch /var/log/rf/rf_control_stdout.log && touch /var/log/rf/rf_control_stderr.log
touch /var/log/rf/ngrok_stdout.log && touch /var/log/rf/ngrok_stderr.log
chown pi:pi /var/log/rf/*

echo "Configuring supervisor..."
echo "##################"
cp config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
supervisord
supervisorctl reload all
supervisorctl start all








