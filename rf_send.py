#!/usr/bin/env python3

import argparse
import logging
from pi_switch import RCSwitchSender

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

parser = argparse.ArgumentParser(description='Sends a decimal code via a 433/315MHz GPIO device')
parser.add_argument('code', metavar='CODE', type=int,
                    help="Decimal code to send")
parser.add_argument('-g', dest='gpio', type=int, default=0,
                    help="GPIO pin according to WiringPi pinout (Default: 0)")
parser.add_argument('-p', dest='pulselength', type=int, default=24,
                    help="Pulselength (Default: 24)")
args = parser.parse_args()

sender = RCSwitchSender()
sender.enableTransmit(args.gpio)
sender.sendDecimal(args.code, args.pulselength)
