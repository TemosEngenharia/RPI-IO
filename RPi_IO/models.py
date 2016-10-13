# -*- coding: utf-8 -*-
from os import path
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Sequence
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from migrate.versioning import api
from sqlalchemy.ext.declarative import declarative_base

APP_DIR = path.dirname(path.realpath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/../../var/sqlite/RPi_IO.db' % APP_DIR
SQLALCHEMY_MIGRATE_REPO = '%s/../../var/sqlite/db_repository' % APP_DIR
SQL_DATABASE_PATH = '%s/../../var/sqlite/RPi_IO.db' % APP_DIR

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread':False}, poolclass=StaticPool)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, Sequence('device_id_seq'), primary_key=True)
    name = Column(String(46), nullable=False)
    timeout = Column(Integer, default=5, nullable=False)
    ip_addr = Column(String(16))
    admin_user = Column(String(50))
    admin_passwd = Column(String(32))
    status = Column(Boolean)
    def __init__(self, name, timeout, ip_addr, admin_user, admin_passwd, status):
        self.name = name
        self.timeout = timeout
        self.ip_addr = ip_addr
        self.admin_user = admin_user
        self.admin_passwd = admin_passwd
        self.status = status
    def __repr__(self):
        return "<Device('Dispositivo: %s\n', \
                        'Tempo de reset: %s\n', \
                        'IP: %s\n', \
                        'Admin User: %s\n', \
                        'Password: %s\n', \
                        'Estado: %s\n'\
                        )>" % (self.name,
                               self.timeout,
                               self.ip_addr,
                               self.admin_user,
                               self.admin_passwd,
                               self.status)

class Module(Base):
    __tablename__ = 'module'
    id = Column(Integer, Sequence('module_id_seq'), primary_key=True)
    name = Column(String(8), nullable=False, unique=True)
    slot = Column(Integer, nullable=False)
    gpio = Column(Integer, nullable=False)
    io_type = Column(String(6), default='input')
    rpull = Column(Boolean, default=False)
    status = Column(Boolean, default=False)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=True)
    def __init__(self, name, slot, gpio, io_type, rpull, status, device_id):
        self.name = name
        self.slot = slot
        self.gpio = gpio 
        self.io_type = io_type
        self.rpull = rpull
        self.status = status
        self.device_id = device_id
    def __repr__(self):
        return "<Module('%s', \
                        'Slot: %s', \
                        'BCM Pin: %s', \
                        'Tipo: %s', \
                        'Pull Resistor: %s, \
                        'Status: %s', \
                        'Device: %s'\
                       )>" % (self.name,
                              self.slot,
                              self.gpio,
                              self.io_type,
                              self.rpull,
                              self.status,
                              self.device_id)


class Event_Log(Base):
    __tablename__ = 'event_log'
    id = Column(Integer, primary_key=True)
    create_on = Column(DateTime(timezone=True), server_default=func.now())
    event = Column(String(46), nullable=True)
    description = Column(String(144), nullable=False)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=True)
    module_id = Column(Integer, ForeignKey("module.id"), nullable=True)
    def __init__(self, event, description, device_id, module_id):
        self.event = event
        self.description = description
        self.device_id = device_id
        self.module_id = module_id
    def __repr__(self):
        return "<Event('Evento: %s', \
                       'Descrição: %s', \
                       'Device: %s', \
                       'Módulo: %s\
                      )>" % (self.event,
                             self.description,
                             self.device_id,
                             self.module_id)


def create_db():
    Base.metadata.create_all(engine)

    if not path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
    M1A = Module(name=u'M1A', slot=1, gpio=8, io_type='input', rpull=False, status=False, device_id='')
    M1B = Module(name=u'M1B', slot=1, gpio=7, io_type='input', rpull=False, status=False, device_id='')
    M1C = Module(name=u'M1C', slot=1, gpio=11, io_type='input', rpull=False, status=False, device_id='')
    M2A = Module(name=u'M2A', slot=2, gpio=9, io_type='input', rpull=False, status=False, device_id='')
    M2B = Module(name=u'M2B', slot=2, gpio=10, io_type='input', rpull=False, status=False, device_id='')
    M2C = Module(name=u'M2C', slot=2, gpio=5, io_type='input', rpull=False, status=False, device_id='')
    M3A = Module(name=u'M3A', slot=3, gpio=6, io_type='input', rpull=False, status=False, device_id='')
    M3B = Module(name=u'M3B', slot=3, gpio=12, io_type='input', rpull=False, status=False, device_id='')
    M3C = Module(name=u'M3C', slot=3, gpio=13, io_type='input', rpull=False, status=False, device_id='')
    M4A = Module(name=u'M4A', slot=4, gpio=0, io_type='input', rpull=False, status=False, device_id='')
    M4B = Module(name=u'M4B', slot=4, gpio=1, io_type='input', rpull=False, status=False, device_id='')
    M4C = Module(name=u'M4C', slot=4, gpio=16, io_type='input', rpull=False, status=False, device_id='')
    M5A = Module(name=u'M5A', slot=5, gpio=17, io_type='input', rpull=False, status=False, device_id='')
    M5B = Module(name=u'M5B', slot=5, gpio=18, io_type='input', rpull=False, status=False, device_id='')
    M5C = Module(name=u'M5C', slot=5, gpio=19, io_type='input', rpull=False, status=False, device_id='')
    M6A = Module(name=u'M6A', slot=6, gpio=20, io_type='input', rpull=False, status=False, device_id='')
    M6B = Module(name=u'M6B', slot=6, gpio=21, io_type='input', rpull=False, status=False, device_id='')
    M6C = Module(name=u'M6C', slot=6, gpio=22, io_type='input', rpull=False, status=False, device_id='')
    M7A = Module(name=u'M7A', slot=7, gpio=23, io_type='input', rpull=False, status=False, device_id='')
    M7B = Module(name=u'M7B', slot=7, gpio=24, io_type='input', rpull=False, status=False, device_id='')
    M7C = Module(name=u'M7C', slot=7, gpio=25, io_type='input', rpull=False, status=False, device_id='')
    modules = [M1A, M1B, M1C, M2A, M2B, M2C, M3A, M3B, M3C, M4A, M4B, M4C,
               M5A, M5B, M5C, M6A, M6B, M6C, M7A, M7B, M7C]
    for m in modules:
        session.add(m)
    session.commit()

def migrate_db():
    import imp
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    exec(old_model, tmp_module.__dict__)
    script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, Base.metadata)
    open(migration, "wt").write(script)
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

def upgrade_db():
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

def downgrade_db():
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

def reset_db():
    # engine = create_engine(SQLALCHEMY_DATABASE_URI)
    # Base = declarative_base()
    # Session = sessionmaker(bind=engine)
    # session = Session()

    session.query(Module).filter(Module.name == 'M1A').update({'gpio': 8, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M1B').update({"gpio": 7, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M1C').update({"gpio": 11, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M2A').update({"gpio": 9, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M2B').update({"gpio": 10, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M2C').update({"gpio": 5, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M3A').update({"gpio": 6, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M3B').update({"gpio": 12, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M3C').update({"gpio": 13, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M4A').update({"gpio": 0, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M4B').update({"gpio": 1, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M4C').update({"gpio": 16, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M5A').update({"gpio": 17, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M5B').update({"gpio": 18, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M5C').update({"gpio": 19, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M6A').update({"gpio": 20, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M6B').update({"gpio": 21, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M6C').update({"gpio": 22, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M7A').update({"gpio": 23, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M7B').update({"gpio": 24, 'io_type': 'input'})
    session.query(Module).filter(Module.name == 'M7C').update({"gpio": 25, 'io_type': 'input'})
    session.commit()

if not path.exists(SQL_DATABASE_PATH):
    print 'criando DataBase'
    create_db()

