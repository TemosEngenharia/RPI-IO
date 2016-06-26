from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('secret')

from RPi_IO import rpi_io
from RPi_IO import views
from RPi_IO import forms
