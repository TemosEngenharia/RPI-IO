#!/home/pi/.virtualenvs/RPi-IO/bin/python
from time import sleep
import sys

def main(argv):
    if len(sys.argv) > 2 or len(sys.argv) <= 1:
       print '\nusage: RPi_IO.py start | stop | rebase\n'
    elif str(sys.argv[1]) == 'start':
        start()
    elif str(sys.argv[1]) == 'stop':
        stop()
    elif str(sys.argv[1]) == 'rebase':
        rebase()
    elif str(sys.argv[1]) == 'resetdb':
        resetdb()
    else:
        print '\nusage: RPi_IO.py start | stop | rebase\n'

def start():
    from RPi_IO import rpi_io
    from RPi_IO import models
    from RPi_WEB import app
    rpi_io.modo0()
    print "Modo 1 e 3 segundos"
    sleep(3)
    rpi_io.modo1()
    print "Modo 3 em 10 segundos"
    sleep(10)
    rpi_io.modo3()
    """
    rpi_io.switch_on(rpi_io.M1A)
    sleep(1)
    rpi_io.switch_on(rpi_io.M1B)
    sleep(1)
    rpi_io.switch_on(rpi_io.M1C)
    sleep(1)

    rpi_io.switch_on(rpi_io.M2A)
    sleep(1)
    rpi_io.switch_on(rpi_io.M2B)
    sleep(1)
    rpi_io.switch_on(rpi_io.M2C)
    sleep(1)

    rpi_io.switch_on(rpi_io.M3A)
    sleep(1)
    rpi_io.switch_on(rpi_io.M3B)
    sleep(1)
    rpi_io.switch_on(rpi_io.M3C)
    sleep(5)

    rpi_io.switch_off(rpi_io.M1A)
    sleep(1)
    rpi_io.switch_off(rpi_io.M1B)
    sleep(1)
    rpi_io.switch_off(rpi_io.M1C)
    sleep(1)

    rpi_io.switch_off(rpi_io.M2A)
    sleep(1)
    rpi_io.switch_off(rpi_io.M2B)
    sleep(1)
    rpi_io.switch_off(rpi_io.M2C)
    sleep(1)

    rpi_io.switch_off(rpi_io.M3A)
    sleep(1)
    rpi_io.switch_off(rpi_io.M3B)
    sleep(1)
    rpi_io.switch_off(rpi_io.M3C)
    sleep(5)

    rpi_io.reset_pin(rpi_io.M1A, 1)
    rpi_io.reset_pin(rpi_io.M2A, 3)
    rpi_io.reset_pin(rpi_io.M3A, 5)
    """
    app.run(host='0.0.0.0', port=80, debug = True)

def stop():
    from RPi_IO import rpi_io
    from RPi_IO import models
    rpi_io.cleanup_pins()

def rebase():
    from RPi_IO.models import migrate_db
    migrate_db()

def resetdb():
    from RPi_IO.models import reset_db
    reset_db()

if __name__ == "__main__":
    from RPi_IO import rpi_io
    from RPi_IO import models
    main(sys.argv[1:])

