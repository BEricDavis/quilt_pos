from app import db
from flask_login import UserMixin
from datetime import datetime
# TimestampMixin -

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return f'<User id:{self.id}, description:{self.description}>'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    birthday = db.Column(db.DateTime)
    street1 = db.Column(db.String(64), index=True)
    street2 = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(6), index=True)
    zip = db.Column(db.String(16), index=True)
    country = db.Column(db.String(64), index=True)
    last_purchase = db.Column(db.DateTime)
    reward_points = db.Column(db.Integer)

    purchases = db.relationship(
        'Purchase', secondary='customer_purchases', backref=db.backref('customers', lazy='dynamic'), lazy='dynamic')


    def __repr__(self):
        return f'<Customer id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}>'


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128), index=True)
    cost = db.Column(db.Float(10, 2), default=0)
    price = db.Column(db.Float(10, 2), nullable=False)
    sku = db.Column(db.String(128), nullable=False)
    inventory = db.Column(db.Float(10,3), default=0)
    last_sold = db.Column(db.DateTime())
    serial_number = db.Column(db.String(128))

    def __repr__(self):
        return f'<Item id:{self.id}, sku:{self.sku}, description:{self.description}>'

# TODO: Consider capturing a dict of item.id and item.price at the time of purchase
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id') )
    tax_rate = db.Column(db.Float(2, 2))
    tax = db.Column(db.Float(10, 2))
    subtotal = db.Column(db.Float(10, 2))
    total = db.Column(db.Float(10, 2))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_items = db.Column(db.Integer)

    items = db.relationship(
        'Item', secondary='purchase_items', backref=db.backref('purchase', lazy=True), lazy='dynamic')

    def __repr__(self):
        return f'<Purchase id:{self.id}, customer_id{self.customer_id}, timestamp:{self.timestamp},' \
               f'total_items:{self.total_items}>'

customer_purchases = db.Table('customer_purchases',
                              db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
                              db.Column('purchase_id', db.Integer, db.ForeignKey('purchase.id'), primary_key=True))


purchase_items = db.Table('purchase_items',
                          db.Column('purchase_id', db.Integer, db.ForeignKey('purchase.id'), primary_key=True),
                          db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True))
# to update the database:
# flask db migrate -m"some statement"
# flask db upgrade