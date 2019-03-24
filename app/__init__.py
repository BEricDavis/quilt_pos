from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask.logging import default_handler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging, os
from logging.handlers import RotatingFileHandler
from datetime import datetime

if not os.path.exists('logs'):
    os.mkdir('logs')

fh = RotatingFileHandler('logs/pos.log', maxBytes=100000, backupCount=10)
sh = logging.StreamHandler()
fm = logging.Formatter('%(asctime)s %(levelname)s %(name)s:%(filename)s:%(lineno)d %(message)s')

fh.setFormatter(fm)
sh.setFormatter(fm)
app = Flask(__name__)
app.logger.removeHandler(default_handler)

fh.setLevel(logging.INFO)
sh.setLevel(logging.INFO)

# logger = logging.getLogger('flask')
app.logger.addHandler(fh)
app.logger.addHandler(sh)


app.logger.info('App starting')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

def format_datetime(value, format='full'):
    # https://stackoverflow.com/questions/4830535/python-how-do-i-format-a-date-in-jinja2

    if format == 'full':
        format = '%m/%d/%Y %H:%M'
    if format == 'year':
        format = '%m/%d/%Y'
    else:
        format = '%m/%d'
    try:
        return value.strftime(format)
    except AttributeError as e:
        print(e)
        print('Received: {}'.format(value))
        return None

# def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
#     print('Start')
#     print('[{}]'.format(value))
#     print(type(value))
#     return value.strftime(format)

app.jinja_env.filters['datetimeformat'] = format_datetime

# this goes at the end
from app import forms, routes, models

