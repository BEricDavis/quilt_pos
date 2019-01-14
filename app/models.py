from app import db
from flask_login import UserMixin
# TimestampMixin -

class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
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

    def __repr__(self):
        return f'<Customer customer_id:{self.customer_id}, first_name:{self.first_name}, last_name:{self.last_name}>'