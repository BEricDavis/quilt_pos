from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def format_datetime(value, format='full'):
    # https://stackoverflow.com/questions/4830535/python-how-do-i-format-a-date-in-jinja2
    if format == 'full':
        format = '%m/%d/%Y %H:%M'
    else:
        format = '%m/%d'
    return value.strftime(format)

# def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
#     print('Start')
#     print('[{}]'.format(value))
#     print(type(value))
#     return value.strftime(format)

app.jinja_env.filters['datetimeformat'] = format_datetime

# this goes at the end
from app import forms, routes, models

