import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'var/sqlite3/iodigital/main.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'var/sqlite3/iodifital/db_repository')

WTF_CSRF_ENABLE = True
# SECRET_KEY inside secret.py
# secret.py => include in .gitignore
