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
    rpi_io.main()
    rpi_io.modo0()
    rpi_io.modo1()
    rpi_io.modo3()

def stop():
    from RPi_IO import rpi_io
    from RPi_IO import models
    rpi_io.main()
    rpi_io.cleanup_pins()

def rebase():
    from RPi_IO.models import migrate_db
    migrate_db()

def resetdb():
    from RPi_IO.models import reset_db
    reset_db()

if __name__ == "__main__":
    main(sys.argv[1:])
