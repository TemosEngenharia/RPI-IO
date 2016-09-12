# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from models import session
from models import Device
from models import Module
from models import Event_Log
from time import sleep
from sys import stdout

# Modules pins and description
M1A = session.query(Module).filter(Module.name == 'M1A').first()
M1B = session.query(Module).filter(Module.name == 'M1B').first()
M1C = session.query(Module).filter(Module.name == 'M1C').first()
M2A = session.query(Module).filter(Module.name == 'M2A').first()
M2B = session.query(Module).filter(Module.name == 'M2B').first()
M2C = session.query(Module).filter(Module.name == 'M2C').first()
M3A = session.query(Module).filter(Module.name == 'M3A').first()
M3B = session.query(Module).filter(Module.name == 'M3B').first()
M3C = session.query(Module).filter(Module.name == 'M3C').first()
M4A = session.query(Module).filter(Module.name == 'M4A').first()
M4B = session.query(Module).filter(Module.name == 'M4B').first()
M4C = session.query(Module).filter(Module.name == 'M4C').first()
M5A = session.query(Module).filter(Module.name == 'M5A').first()
M5B = session.query(Module).filter(Module.name == 'M5B').first()
M5C = session.query(Module).filter(Module.name == 'M5C').first()
M6A = session.query(Module).filter(Module.name == 'M6A').first()
M6B = session.query(Module).filter(Module.name == 'M6B').first()
M6C = session.query(Module).filter(Module.name == 'M6C').first()
M7A = session.query(Module).filter(Module.name == 'M7A').first()
M7B = session.query(Module).filter(Module.name == 'M7B').first()
M7C = session.query(Module).filter(Module.name == 'M7C').first()

# Statup inputs BCM pin
input_pins = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25]

# Statup outputs BCM pin
output_pins = [26, 27]

def main():
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)


def modo0():
    for pin in input_pins:
        try:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        except:
             print u"Erro de ativação do Pino BCM %s", pin
             stdout.flush()
    for pin in output_pins:
        try:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        except:
             print u"Erro na ativação do Pino BCM %s", pin
             stdout.flush()
    return(True)

def modo1():
    global M1A, M1B, M1C
    global M2A, M2B, M2C
    global M3A, M3B, M3C
    global M4A, M4B, M4C
    global M5A, M5B, M5C
    global M6A, M6B, M6C
    global M7A, M7B, M7C
    
    try:
        GPIO.output(26, GPIO.HIGH)
    except:
         print u'Erro ao setar o nível do pino BCM pin 26'
    try:
        GPIO.output(27, GPIO.LOW)
    except:
         print u'Erro ao setar o nível do pino BCM pin 27'

    sleep(5)
    discovery_mods(M1A, M1B, M1C)
    discovery_mods(M2A, M2B, M2C)
    discovery_mods(M3A, M3B, M3C)
    discovery_mods(M4A, M4B, M4C)
    discovery_mods(M5A, M5B, M5C)
    discovery_mods(M6A, M6B, M6C)
    discovery_mods(M7A, M7B, M7C)
       

def modo3():
    try:
        GPIO.output(26, GPIO.HIGH)
    except:
        print u'Erro ao setar o nível do pino BCM pin 26'
    try:
        GPIO.output(27, GPIO.HIGH)
    except:
        print u'Erro ao setar o nível do pino BCM pin 27'
    return  True

def switch_on(_M):
    import RPi.GPIO as GPIO
    from models import session
    from models import Device
    from models import Module
    from models import Event_Log
    from time import sleep
    from sys import stdout
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    if GPIO.gpio_function(_M.gpio) == 0:
        GPIO.setup(_M.gpio, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(_M.gpio, GPIO.HIGH)
        _M.status = True
        session.commit()
    else:
        print 'ERROR! This pin is set as a input'


def switch_off(_M):
    import RPi.GPIO as GPIO
    from models import session
    from models import Device
    from models import Module
    from models import Event_Log
    from time import sleep
    from sys import stdout
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    if GPIO.gpio_function(_M.gpio) == 0:
        GPIO.setup(_M.gpio, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(_M.gpio, GPIO.LOW)
        _M.status = False
        session.commit()
    else:
        print 'ERROR! This pin is set as a input'

def reset_pin(_M, _time):
    import RPi.GPIO as GPIO
    from models import session
    from models import Device
    from models import Module
    from models import Event_Log
    from time import sleep
    from sys import stdout
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    if GPIO.gpio_function(_M.gpio) == 0:
        switch_on(_M)
        sleep(_time)
        switch_off(_M)
    else:
        print 'ERROR! This pin is set as a input'

def discovery_mods(_MA, _MB, _MC):
    import RPi.GPIO as GPIO
    from models import session
    from models import Device
    from models import Module
    from models import Event_Log
    from time import sleep
    from sys import stdout
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    if GPIO.input(_MA.gpio) == 0 and GPIO.input(_MB.gpio) == 1:
        GPIO.setup(_MA.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(_MB.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(_MC.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        _MA.io_type = 'input'
        _MA.rpull = False
        _MB.io_type = 'input'
        _MB.rpull = False
        _MC.io_type = 'input'
        _MC.rpull = False
        session.commit()
    elif GPIO.input(_MA.gpio) == 1 and GPIO.input(_MB.gpio) == 0:
        GPIO.setup(_MA.gpio, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(_MB.gpio, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(_MC.gpio, GPIO.OUT, initial=GPIO.LOW)
        _MA.io_type = 'output'
        _MA.status = False
        _MB.io_type = 'output'
        _MB.status = False
        _MC.io_type = 'output'
        _MC.status = False
        session.commit()
    else:
        GPIO.setup(_MA.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(_MB.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(_MC.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        _MA.io_type = 'empty'
        _MA.rpull = False
        _MB.io_type = 'empty'
        _MB.rpull = False
        _MC.io_type = 'empty'
        _MC.rpull = False
        session.commit()

def cleanup_pins():
    import RPi.GPIO as GPIO
    from models import session
    from models import Device
    from models import Module
    from models import Event_Log
    from time import sleep
    from sys import stdout
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()

if __name__ == "__main__":
    main()

