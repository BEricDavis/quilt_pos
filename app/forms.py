from flask_wtf import FlaskForm
from app import app
from datetime import datetime
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, ValidationError, Email
from wtforms.ext.dateutil.fields import DateField, DateTimeField
from wtforms.ext import dateutil
from app.models import Customer

class NewCustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    street1 = StringField('Address 1')
    street2 = StringField('Address 2')
    city = StringField('City')
    state = StringField('State')
    zip = StringField('Zip')
    phone = StringField('Phone')
    birthday = DateField('Birthday (mm/dd)', default=app.config['DATEUTIL_DEFAULT'])

    submit = SubmitField('Add')

    # def validate_birthday(self, birthday):
    #     # stub for birthday validations
    #     if birthday is not None:
    #         pass


class NewItemForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    sku = StringField('SKU', validators=[DataRequired()])
    item_number = StringField('Shop Item Number', validators=[DataRequired()])
    quantity = FloatField('Quantity', validators=[DataRequired()])
    cost = FloatField('Cost')
    price = FloatField('Price', validators=[DataRequired()])

    submit = SubmitField('Add')