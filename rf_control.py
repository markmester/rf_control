import logging
from flask import Flask, render_template
from flask_ask import Ask, statement
from utils import get_device
import subprocess
import yaml


with open('config/config.yaml', 'r+') as f:
    config = yaml.load(f)

app = Flask(__name__)
ask = Ask(app, "/")
gpio_out = config['gpio_out'] # pin used to transmit rf codes

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)




@ask.intent("DeviceOn", mapping={'device': 'device'})
def device_on(device):
    on_msg = render_template('device_on', device=device)
    device = get_device(device)

    cmd = "python3 rf_send.py {} -p {} -g {}".format(device['on_code'],
                                                           device['pulse_width'],
                                                           gpio_out)

    try:
        subprocess.check_call(cmd.split())
    except subprocess.CalledProcessError as e:
        logging.error("Failed to send rf code; {}".format(e))

    return statement(on_msg)


@ask.intent("DeviceOff", mapping={'device': 'device'})
def device_off(device):
    off_msg = render_template('device_off', device=device)
    device = get_device(device)

    cmd = "python3 rf_send.py {} -p {} -g {}".format(device['off_code'],
                                                           device['pulse_width'],
                                                           gpio_out)

    try:
        subprocess.check_call(cmd.split())
    except subprocess.CalledProcessError as e:
        logging.error("Failed to send rf code; {}".format(e))


    return statement(off_msg)

if __name__ == '__main__':
    app.run(debug=True)