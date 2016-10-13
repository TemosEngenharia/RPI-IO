#!/var/ramdisk/RPi-IO/venv/bin/python
# -*- coding: utf-8 -*-
import sys
import os.path
import logging
import RPi.GPIO as GPIO
from models import session
from models import Device
from models import Module
from models import Event_Log
from rpi_io import reset_pin as reboot
from time import sleep

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
M5B = session.query(Module).filter(Module.name == 'M5B').first()
M5C = session.query(Module).filter(Module.name == 'M5C').first()
ADSL = M5B
HONGDIAN = M5C
SEMPARAR_ADDR = '172.19.254.254'
HONGDIAN_ADDR = '172.19.254.1'
NET_ADDR = '8.8.8.8'

logging.basicConfig(filename='/var/log/net_mon',level=logging.DEBUG)

def main(argv):
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
       print '\nusage: net_mon.py start | stop\n'
    elif str(sys.argv[1]) == 'start':
        start()
    elif str(sys.argv[1]) == 'stop':
        stop()
    elif str(sys.argv[1]) == 'check':
        check(sys.argv[2])
    else:
        print '\nusage: net_mon.py start | stop\n'

def check(_ADDR):
    # Perform the ping using the system ping command (one ping only)
    rawPingFile = os.popen('/bin/ping -c 5 %s' % (_ADDR))
    rawPingData = rawPingFile.readlines()
    rawPingFile.close()
    # Extract the ping time
    len_raw = len(rawPingData)
    if len_raw < 5:
        return False
    else:
        index = rawPingData[len_raw - 2].find('%')
        if index == -1:
            return False
        else:
            packet_loss = rawPingData[len_raw - 2][index - 4:index]
            packet_loss = int(packet_loss[packet_loss.find(' '):])
            logging.info('Packet Loss: %s', packet_loss)
            if packet_loss > 50:
                return False
            else:
                return True

def start():
    while True:
        if check(NET_ADDR):
            if check(SEMPARAR_ADDR):
                logging.info("Tudo OK")
            else:
                logging.info("Problema somente Sem Parar: " + SEMPARAR_ADDR)
                reboot(HONGDIAN, 10)
                sleep(600)
        else:
            if check(HONGDIAN_ADDR) and check(SEMPARAR_ADDR):
                logging.info("Problema somente Internet")
                reboot(ADSL, 10)
                sleep(600)
            else:
                logging.info("Problema HONGDIAN para frente")
                reboot(ADSL, 10)
                reboot(HONGDIAN, 10)
                sleep(600)


def stop():
    GPIO.cleanup()

if __name__ == "__main__":
    main(sys.argv[1:])

