# RPI RF Control

!!!! NEEDS UPDATING

### Hardware
- Raspbery Pi3
- Etekcity Wireless Remote Control Electrical Outlet Switch
- UCEC XY-MK-5V / XY-FST 433Mhz Rf Transmitter and Receiver Link

### Dependencies
```
# apt install python3-pip supervisor
# pip3 install rpi-rf pyaml flask flask-ast

```
_Run ```sudo ./install.sh``` to auto install dependencies and create log dirs/files_


### Setup
###### GPIO Pinouts
transmitter | pi
- - - - - - - - -
5V5 | 5V5
GND | GND
DATA | GPIO23

receiver | pi
- - - - - - - - -
3V3 | 3V3
GND | GND
DATA | GPIO23

1. Using the above pinout, hook up the rf receiver unit to the Raspberry Pi 3.
2. Run the rf_receive.py script, press the on/off buttons on your rf switch remote, and record the code, pulse length, and protocol
```
sudo python3 rf_receive.py -g 23
```
3. Modify the config.yaml file to include the recorded devices on/off codes, pulse length, and protocol
4. Hook up the rf transmitter unit according to the above pinout.
5. On the raspberry pi, run rf_control.py:
```
python rf_control.pi
```
6. On the Raspberry Pi, unzip the ngrok zip file:
```
unzip /path/to/ngrok.zip
```

7. Run ngrok:
```
./ngrok http 5000
```
Make note of the last HTTPS endpoint.
8. In your amazon developers account, go to Alexa > Add Skill
9. In 'Skill Information', set the following:
- Name: Device Control
- Invocation Name: Device Control
10. In 'Interaction Model', set the following, copy/paste the intent_schema.json and sample_utterances.txt into the appropriate fields.
11. Still under 'Interaction Model', click 'Add Slot Type'. Configure the following:
- Enter Type: DEVICES
- Enter Values: <line separted list of device names> e.g.:
```
living room lights
lights in the living room
lights
the lights
```
12. In 'Configuration', set the Service Endpoint Type to HTTPS and enter the ngrok https url recorded previously for the service endpoint.
13. In 'SSL Certificate' select the wildcard certificate option.
14. That's it! Go test your new skill.
