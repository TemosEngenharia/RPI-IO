# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
from sys import stdout

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

AC01 = 23
AC02 = 24
AC03 = 25


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
    elif GPIO.input(AC01) == True:
        AC01_NOK = AC01_NOK + 1
        AC01_OK = 0
        if AC01_NOK >= 120:
            print("AC01 - Energia fora")
            AC01_NOK = 0
    if GPIO.input(AC02) == False:
        AC02_OK = AC02_OK + 1
        AC02_NOK = 0
    elif GPIO.input(AC02) == True:
        AC02_NOK = AC02_NOK + 1
        AC02_OK = 0
        if AC02_NOK >= 120:
            # print("AC02 - Energia fora")
            AC02_NOK = 0
    if GPIO.input(AC03) == False:
        AC03_OK = AC03_OK + 1
        AC03_NOK = 0
    elif GPIO.input(AC03) == True:
        AC03_NOK = AC03_NOK + 1
        AC03_OK = 0
        if AC03_NOK >= 120:
            # print("AC03 - Energia fora")
            AC03_NOK = 0
    sleep(0.01666666667)
GPIO.cleanup()

