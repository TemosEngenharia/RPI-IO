#!/home/pi/.virtualenvs/RPi-IO/bin/python

from RPi_WEB import app
from RPi_WEB import views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

