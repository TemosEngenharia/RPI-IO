import subprocess
from flask import render_template
from flask import redirect
from RPi_IO.rpi_io import switch_on
from RPi_IO.rpi_io import switch_off
from RPi_IO.rpi_io import reset_pin
from RPi_IO.rpi_io import softreset
from RPi_IO.models import Device
from RPi_IO.models import Module
from RPi_IO.models import Event_Log
from RPi_IO.models import session
from RPi_WEB import app

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

M1 = [M1A, M1B, M1C]
M2 = [M2A, M2B, M2C]
M3 = [M3A, M3B, M3C]
M4 = [M4A, M4B, M4C]
M5 = [M5A, M5B, M5C]
M6 = [M6A, M6B, M6C]
M7 = [M7A, M7B, M7C]

modules = [M1A, M1B, M1C,
           M2A, M2B, M2C,
           M3A, M3B, M3C,
           M4A, M4B, M4C,
           M5A, M5B, M5C,
           M6A, M6B, M6C,
           M7A, M7B, M7C]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/opr")
def opr():
    return render_template('opr_abastece.html', M1=M1, M2=M2, M3=M3, M4=M4, M5=M5, M6=M6, M7=M7, modules=modules)

@app.route("/<mod_name>/<action>")
def action(mod_name, action):
    for mod in modules:
        if mod_name == mod.name:
            if action == 'on':
               switch_on(mod)
            if action == 'off':
               switch_off(mod)
            if action == 'reset':
               reset_pin(mod, 3)
            if action == 'softreset':
               if mod.name ==  'M3C':
                   cmd = '/usr/bin/net rpc shutdown -r -f -t 1 -I 192.168.1.21 -U Administrador%SemParar'
                   p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
                   out,err = p.communicate()
                   if err:
                       return err
               elif mod.name == 'M5A':
                   cmd = '/usr/bin/net rpc shutdown -r -f -t 1 -I 192.168.1.10 -U Administrador%SemParar'
                   p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
                   out,err = p.communicate()
                   if err:
                       return err
    return redirect("/opr")

@app.route('/cad')
def cad():
    return render_template('cad.html')

@app.route('/log')
def log():
    return render_template('log.html')

