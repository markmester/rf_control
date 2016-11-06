import logging
from flask import Flask, render_template
from flask_ask import Ask, statement
import subprocess

app = Flask(__name__)
ask = Ask(app, "/")
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)


@ask.intent("DeviceOn", mapping={'device': 'device'})
def device_on(device):
    on_msg = render_template('device_on', device=device)

    cmd = "python3 rf_send.py 5526835 -g 26 -p 183"

    try:
        subprocess.check_call(cmd.split())
    except subprocess.CalledProcessError as e:
        logging.error("Failed to send rf code; {}".format(e))

    return statement(on_msg)


@ask.intent("DeviceOff", mapping={'device': 'device'})
def device_off(device):
    off_msg = render_template('device_off', device=device)

    cmd = "python3 rf_send.py 5526844 -g 26 -p 183"

    try:
        subprocess.check_call(cmd.split())
    except subprocess.CalledProcessError as e:
        logging.error("Failed to send rf code; {}".format(e))


    return statement(off_msg)

if __name__ == '__main__':
    app.run(debug=True)