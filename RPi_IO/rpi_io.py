# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from models import session
from models import Device
from models import Module
from models import Event_Log
from time import sleep
from sys import stdout

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
sleep(3)

# Modules pins and description
"""
Listagem do atributos dos módulos no SQLite
M1A = Module(name=u'Módulo 1A', slot=1, gpio=5, io_type='input', rpull=False, status=False, device_id='')
M1B = Module(name=u'Módulo 1B', slot=1, gpio=6, io_type='input', rpull=False, status=False, device_id='')
M1C = Module(name=u'Módulo 1C', slot=1, gpio=7, io_type='input', rpull=False, status=False, device_id='')
M2A = Module(name=u'Módulo 2A', slot=2, gpio=8, io_type='input', rpull=False, status=False, device_id='')
M2B = Module(name=u'Módulo 2B', slot=2, gpio=9, io_type='input', rpull=False, status=False, device_id='')
M2C = Module(name=u'Módulo 2C', slot=2, gpio=10, io_type='input', rpull=False, status=False, device_id='')
M3A = Module(name=u'Módulo 3A', slot=3, gpio=11, io_type='input', rpull=False, status=False, device_id='')
M3B = Module(name=u'Módulo 3B', slot=3, gpio=12, io_type='input', rpull=False, status=False, device_id='')
M3C = Module(name=u'Módulo 3C', slot=3, gpio=13, io_type='input', rpull=False, status=False, device_id='')
M4A = Module(name=u'Módulo 4A', slot=4, gpio=0, io_type='input', rpull=False, status=False, device_id='')
M4B = Module(name=u'Módulo 4B', slot=4, gpio=1, io_type='input', rpull=False, status=False, device_id='')
M4C = Module(name=u'Módulo 4C', slot=4, gpio=16, io_type='input', rpull=False, status=False, device_id='')
M5A = Module(name=u'Módulo 5A', slot=5, gpio=17, io_type='input', rpull=False, status=False, device_id='')
M5B = Module(name=u'Módulo 5B', slot=5, gpio=18, io_type='input', rpull=False, status=False, device_id='')
M5C = Module(name=u'Módulo 5C', slot=5, gpio=19, io_type='input', rpull=False, status=False, device_id='')
M6A = Module(name=u'Módulo 6A', slot=6, gpio=20, io_type='input', rpull=False, status=False, device_id='')
M6B = Module(name=u'Módulo 6B', slot=6, gpio=21, io_type='input', rpull=False, status=False, device_id='')
M6C = Module(name=u'Módulo 6C', slot=6, gpio=22, io_type='input', rpull=False, status=False, device_id='')
M7A = Module(name=u'Módulo 7A', slot=7, gpio=23, io_type='input', rpull=False, status=False, device_id='')
M7B = Module(name=u'Módulo 7B', slot=7, gpio=24, io_type='input', rpull=False, status=False, device_id='')
M7C = Module(name=u'Módulo 7C', slot=7, gpio=25, io_type='input', rpull=False, status=False, device_id='')

modules = [M1A, M1B, M1C, M2A, M2B, M2C, M3A, M3B, M3C, M4A, M4B, M4C,
           M5A, M5B, M5C, M6A, M6B, M6C, M7A, M7B, M7C]
# for m in modules:
    # session.add(m)
    # session.commit()
"""
modules = {
           1 : {'PinA' : 5, 'PinB' : 6, 'PinC' : 7, 'Name' : u'Módulo 1', 'Tipo' : 'input'},
           2 : {'PinA' : 8, 'PinB' : 9, 'PinC' : 10, 'Name' : u'Módulo 2', 'Tipo' : 'input'},
           3 : {'PinA' : 11, 'PinB' : 12, 'PinC' : 13, 'Name' : u'Módulo 3', 'Tipo' : 'input'},
           4 : {'PinA' : 0, 'PinB' : 1, 'PinC' : 16, 'Name' : u'Módulo 4', 'Tipo' : 'input'},
           5 : {'PinA' : 17, 'PinB' : 18, 'PinC' : 19, 'Name' : u'Módulo 5', 'Tipo' : 'input'},
           6 : {'PinA' : 20, 'PinB' : 21, 'PinC' : 22, 'Name' : u'Módulo 6', 'Tipo' : 'input'},
           7 : {'PinA' : 23, 'PinB' : 24, 'PinC' : 25, 'Name' : u'Módulo 7', 'Tipo' : 'input'}
          }

# Statup inputs BCM pin
input_pins = [0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25]

# Statup outputs BCM pin
output_pins = [26, 27]

def modo0():
    # print "Entrando em modo 0"
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
    return(True)

def modo1():
    # print "\n\nEntrando em modo 1"
    global modules
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

    # print u'\nDescorberta do módulos' 
    timer = 1
    while timer <= 5:
        for module in modules:
            # stdout.flush()
            # stdout.write('.') 
            # print module[3], u'Pino A: ', GPIO.input(module[0]), u'Pino B: ', GPIO.input(module[1])
            if GPIO.input(modules[module]['PinA']) == 1 and GPIO.input(modules[module]['PinB']) == 0:
                # print module[3], u' é um módulo de entradas'
                GPIO.setup(modules[module]['PinA'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(modules[module]['PinB'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(modules[module]['PinC'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                modules[module]['Tipo'] = u'input'
            elif GPIO.input(modules[module]['PinA']) == 0 and GPIO.input(modules[module]['PinB']) == 1:
                # print module[3], u' é um módulo de saídas'
                GPIO.setup(modules[module]['PinA'], GPIO.OUT, initial=GPIO.LOW)
                GPIO.setup(modules[module]['PinB'], GPIO.OUT, initial=GPIO.LOW)
                GPIO.setup(modules[module]['PinC'], GPIO.OUT, initial=GPIO.LOW)
                modules[module]['Tipo'] = u'output'
            elif GPIO.input(modules[module]['PinA']) == 0 and GPIO.input(modules[module]['PinB']) == 0:
                # print module[3], u' não está populado'
                GPIO.setup(modules[module]['PinA'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(modules[module]['PinB'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                GPIO.setup(modules[module]['PinC'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                modules[module]['Tipo'] = u'empty'
        sleep(1)
        timer = timer + 1
    # print u'.OK'
    # sleep(0.5)
    # for module in modules:
        # print modules[module]['Name']
        # print '    ', modules[module]['Tipo']
        # print '    ', modules[module]['PinA'], GPIO.gpio_function(modules[module]['PinA'])
        # print '    ', modules[module]['PinB'], GPIO.gpio_function(modules[module]['PinB'])
        # print '    ', modules[module]['PinC'], GPIO.gpio_function(modules[module]['PinC'])

    # print u'Mudando para modo 3 em:',

    # for i in [5, 4, 3, 2, 1]:
        # stdout.flush()
        # print i,
        # sleep(1)
    return(True)
       

def modo3():
    # print "\n\nEntrando em modo 3"
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
    return  True

def switch_on(_pin):
    if GPIO.gpio_function(_pin) == 0:
        GPIO.output(_pin, GPIO.HIGH)
    else:
        print 'ERROR! This pin is set as a input'


def switch_off(_pin):
    if GPIO.gpio_function(_pin) == 0:
        GPIO.output(_pin, GPIO.LOW)
    else:
        print 'ERROR! This pin is set as a input'

def reset_pin(_pin, _time):
    if GPIO.gpio_function(_pin) == 0:
        switch_on(_pin)
        sleep(_time)
        switch_off(_pin)
    else:
        print 'ERROR! This pin is set as a input'

def cleanup_pins():
    GPIO.cleanup()

