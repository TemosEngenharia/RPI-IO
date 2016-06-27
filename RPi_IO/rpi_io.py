# -*- coding: utf-8 -*-
from time import sleep
from sys import stdout
import RPi.GPIO as GPIO

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
sleep(3)

# Modules pins and description
M1 = [5, 6, 7, u'Módulo 1', 'tipo']
M2 = [8, 9, 10, u'Módulo 2', 'tipo']
M3 = [11, 12, 13, u'Módulo 3', 'tipo']
M4 = [0, 1, 16, u'Módulo 4', 'tipo']
M5 = [17, 18, 19,  u'Módulo 5', 'tipo']
M6 = [20, 21, 22, u'Módulo 6', 'tipo']
M7 = [23, 24, 25, u'Módulo 7', 'tipo']

# Statup inputs BCM pin
input_pins = [0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25]

# Statup outputs BCM pin
output_pins = [26, 27]

def modo0():
    print "Entrando em modo 0"
    for pin in input_pins:
        try:
            # print u'Configurando o pino BCM ', pin,' como entrada'
            # stdout.flush()
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        except:
            print u"Erro de ativação do Pino BCM %s", pin
            stdout.flush()
    for pin in output_pins:
        try:
            # print u'Configurando o pino BCM ', pin,' como saída'
            # stdout.flush()
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        except:
            print u"Erro na ativação do Pino BCM %s", pin
            stdout.flush()
    modo1()


def modo1():
    print "\n\nEntrando em modo 1"
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6
    global M7
    mods = [M1, M2, M3, M4, M5, M6, M7]
    try:
        # print u'Setando o pino de SETUP0 (BCM pin 26) para o valor HIGH'
        GPIO.output(26, GPIO.HIGH)
    except:
        print u'Erro ao setar o nível do pino BCM pin 26'
    try:
        # print u'Setando o pino de SETUP1 (BCM pin 27) para o valor LOW'
        GPIO.output(27, GPIO.LOW)
    except:
        print u'Erro ao setar o nível do pino BCM pin 27'

    print u'\nDescorberta do módulos' 
    timer = 1
    while timer <= 5:
        for module in mods:
            stdout.flush()
            stdout.write('.') 
            # print module[3], u'Pino A: ', GPIO.input(module[0]), u'Pino B: ', GPIO.input(module[1])
            if GPIO.input(module[0]) == 1 and GPIO.input(module[1]) == 0:
                # print module[3], u' é um módulo de entradas'
                GPIO.setup(module[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(module[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(module[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                module[4] = u'input'
            elif GPIO.input(module[1]) == 1 and GPIO.input(module[0]) == 0:
                # print module[3], u' é um módulo de saídas'
                GPIO.setup(module[0], GPIO.OUT, initial=GPIO.LOW)
                GPIO.setup(module[1], GPIO.OUT, initial=GPIO.LOW)
                GPIO.setup(module[2], GPIO.OUT, initial=GPIO.LOW)
                module[4] = u'output'
            elif GPIO.input(module[0]) == 0 and GPIO.input(module[1]) == 0:
                # print module[3], u' não está populado'
                GPIO.setup(module[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(module[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(module[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                module[4] = u'open'
            sleep(0.1)
        timer = timer + 1
    print u'.OK'
    sleep(0.5)
    for i in [M1, M2, M3, M4, M5, M6, M7]:
        print i[3],i[4]

    print u'Mudando para modo 3 em:',

    for i in [5, 4, 3, 2, 1]:
        stdout.flush()
        print i,
        sleep(1)
       
    modo3()

def modo3():
    print "\n\nEntrando em modo 3"
    try:
        # print u'Setando o pino de SETUP0 (BCM pin 26) para o valor HIGH'
        GPIO.output(26, GPIO.HIGH)
    except:
        print u'Erro ao setar o nível do pino BCM pin 26'
    try:
        # print u'Setando o pino de SETUP1 (BCM pin 27) para o valor HIGH'
        GPIO.output(27, GPIO.HIGH)
    except:
        print u'Erro ao setar o nível do pino BCM pin 27'
    sleep(5)
    GPIO.cleanup()
