from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('secret')
db = SQLAlchemy(app)

from RPi_IO import forms
from RPi_IO import views
from RPi_IO import rpi_io
