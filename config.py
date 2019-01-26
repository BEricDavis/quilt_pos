import os
from datetime import datetime
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # flask-sqlalchemy configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'pos.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mail server configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['some-email@example.com']

    # Pagination
    CUSTOMERS_PER_PAGE = 3
    ITEMS_PER_PAGE = 3

    # dateutil config
    DATEUTIL_DEFAULT = datetime(1972, 1, 1)