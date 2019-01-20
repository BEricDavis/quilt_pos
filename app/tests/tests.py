from app import app, db
import unittest
from datetime import datetime
from app.models import Customer, Item, Purchase, User
import sys


def setUpModule():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    print('in setUp\n')
    db.create_all()


def tearDownModule():
    db.session.remove()
    print('in tearDown')
    db.drop_all()

class PurchaseModelCase(unittest.TestCase):


    def test_customer_creation(self):
        print('in test_customer\n')
        c = Customer(first_name='Jessica',
                     last_name='Smith',
                     email='quilt2@feralmonkey.net',
                     birthday=datetime.utcnow(),
                     street1='123 N. Main St.',
                     street2='',
                     city='Miamisburg',
                     state='OH',
                     zip='45342',
                     country='US',
                     last_purchase=datetime.utcnow(),
                     reward_points=0)
        db.session.add(c)
        db.session.commit()

    def test_item_creation(self):

        i1 = Item(description='red fabric',
                  cost=4.99,
                  price=9.99,
                  sku='123456789A',
                  last_sold=datetime.utcnow(),
                  inventory=15)
        i2 = Item(description='blue fabric',
                  cost=5.00,
                  price=10.00,
                  sku='abc-def-123',
                  last_sold=datetime.utcnow(),
                  inventory=15)
        db.session.add(i1)
        db.session.add(i2)
        db.session.commit()

    def test_purchase(self):
        print('In test_purchase')
        customer = Customer.query.filter_by(email='quilt2@feralmonkey.net').first()
        c2 = Customer.query.filter_by(email='quilt2@feralmonkey.net').all()
        print('c2: {}'.format(c2))
        item1 = Item.query.filter_by(sku='123456789A').first()
        print('item1: {}'.format(item1))
        item2 = Item.query.filter_by(sku='abc-def-123').first()
        print('item2: {}'.format(item2))
        subtotal = item1.price + item2.price
        tax = float(subtotal) * .075
        total = float(subtotal) + tax


        p = Purchase(
            customer_id=customer,
            items=[item1, item2],
            total_items=2,
            tax=tax,
            subtotal=subtotal,
            total=total
        )
        print('purchase: {}'.format(p))
        db.session.add(p)
        db.session.commit()
        p1 = Purchase.query.filter_by(id=1)
        print('purhcase: {}'.format(p1))


if __name__ == '__main__':
    unittest.main(verbosity=2)