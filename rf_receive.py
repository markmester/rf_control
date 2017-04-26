#!/usr/bin/env python

from pi_switch import RCSwitchReceiver
import argparse
import logging

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

parser = argparse.ArgumentParser(description='Listens for rf codes via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=2,
                    help="GPIO pin according to WiringPi pinout (Default: 17)")
args = parser.parse_args()

receiver = RCSwitchReceiver()
receiver.enableReceive(args.gpio)

num = 0

while True:
    if receiver.available():
        received_value = receiver.getReceivedValue()
        if received_value:
            num += 1
            print("Received[%s]:" % num)
            print(received_value)
            print("%s / %s bit" % (received_value, receiver.getReceivedBitlength()))
            print("Protocol: %s" % receiver.getReceivedProtocol())
            print("")

        receiver.resetAvailable()