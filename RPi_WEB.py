#!/var/ramdisk/RPi-IO/venv/bin/python
import cherrypy
import time
from paste.translogger import TransLogger
from cherrypy.process.plugins import Daemonizer
from RPi_WEB import app
from RPi_WEB import views

class FotsTransLogger(TransLogger):
    def write_log(self, environ, method, req_uri, start, status, bytes):
        if bytes is None:
            bytes = '-'
        remote_addr = '-'
        if environ.get('HTTP_X_FORWARDED_FOR'):
            remote_addr = environ['HTTP_X_FORWARDED_FOR']
        elif environ.get('REMOTE_ADDR'):
            remote_addr = environ['REMOTE_ADDR']
        d = {
            'REMOTE_ADDR': remote_addr,
            'REMOTE_USER': environ.get('REMOTE_USER') or '-',
            'REQUEST_METHOD': method,
            'REQUEST_URI': req_uri,
            'HTTP_VERSION': environ.get('SERVER_PROTOCOL'),
            'time': time.strftime('%d/%b/%Y:%H:%M:%S', start),
            'status': status.split(None, 1)[0],
            'bytes': bytes,
            'HTTP_REFERER': environ.get('HTTP_REFERER', '-'),
            'HTTP_USER_AGENT': environ.get('HTTP_USER_AGENT', '-'),
        }
        message = self.format % d
        self.logger.log(self.logging_level, message)

def run_server():
    app_logged = TransLogger(app)
    #Daemonizer(cherrypy.engine).subscribe()
    cherrypy.tree.graft(app_logged, '/')
    cherrypy.config.update({
        'engine.autoreload.on': True,
        'log.screen': True,
        'server.socket_port': 8080,
        'server.socket_host': '0.0.0.0'
    })
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == "__main__":
    run_server()

