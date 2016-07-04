from flask import Flask

app = Flask(__name__)

import RPi_WEB.models
import RPi_WEB.views

