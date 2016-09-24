# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from models import session
from models import Device
from models import Module
from models import Event_Log
from time import sleep

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

M7A = session.query(Module).filter(Module.name == 'M7A').first()
M7B = session.query(Module).filter(Module.name == 'M7B').first()
M7C = session.query(Module).filter(Module.name == 'M7C').first()

M7A.status = True
M7B.status = True
M7C.status = True
session.commit()

AC01 = M7A.gpio
AC02 = M7B.gpio
AC03 = M7C.gpio


GPIO.setup(AC01, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(AC02, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(AC03, GPIO.IN, GPIO.PUD_UP)
AC01_OK=0
AC01_NOK=0
AC02_OK=0
AC02_NOK=0
AC03_OK=0
AC03_NOK=0

while True:
    if GPIO.input(AC01) == False:
        AC01_OK = AC01_OK + 1
        AC01_NOK = 0
        if M7A.status == True:
            M7A.status = False
            session.commit()
            print("AC01 - Energia ligada")
            print M7A
    elif GPIO.input(AC01) == True:
        AC01_NOK = AC01_NOK + 1
        AC01_OK = 0
        if AC01_NOK >= 120 and M7A.status == False:
            M7A.status = True
            session.commit()
            print("AC01 - Energia desligada")
            print M7A
            AC01_NOK = 0
    if GPIO.input(AC02) == False:
        AC02_OK = AC02_OK + 1
        AC02_NOK = 0
        if M7B.status == True:
            M7B.status = False
            session.commit()
            print("AC02 - Energia ligada")
            print M7B
    elif GPIO.input(AC02) == True:
        AC02_NOK = AC02_NOK + 1
        AC02_OK = 0
        if AC02_NOK >= 120 and M7B.status == False:
            M7B.status = True
            session.commit()
            print("AC02 - Energia desligada")
            print M7B
            AC02_NOK = 0
    if GPIO.input(AC03) == False:
        AC03_OK = AC03_OK + 1
        AC03_NOK = 0
        if M7C.status == True:
            M7C.status = False
            session.commit()
            print("AC03 - Energia ligada")
            print M7A
    elif GPIO.input(AC03) == True:
        AC03_NOK = AC03_NOK + 1
        AC03_OK = 0
        if AC03_NOK >= 120 and M7C.status == False:
            M7B.status = True
            session.commit()
            print("AC03 - Energia desligada")
            AC03_NOK = 0
    sleep(0.01666666667)
GPIO.cleanup()

