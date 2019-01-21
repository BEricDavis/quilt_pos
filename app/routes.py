from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Customer, Item
from app.forms import NewCustomerForm, NewItemForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    form = NewCustomerForm()


    if form.validate_on_submit():
        print('validated')
        customer = Customer(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            #birthday=form.birthday.data,
                            street1=form.street1.data,
                            street2=form.street2.data,
                            city=form.city.data,
                            state=form.state.data,
                            zip=form.zip.data
                            )
        db.session.add(customer)
        db.session.commit()
        flash('Customer added')
        return redirect(url_for('index'))
    else:
        print('not validated')

    return render_template('customer_add.html', title='Add new customer', form=form)

@app.route('/item/add', methods=['GET', 'POST'])
def item_add():
    form = NewItemForm()

    if form.validate_on_submit():
        item = Item(description=form.description.data,
                    sku=form.sku.data,
                    item_number=form.item_number.data,
                    quantity=form.quantity.data,
                    cost=form.cost.data,
                    price=form.price.data)
        db.session.add(item)
        db.session.commit()
        flash('Item added')
        return redirect(url_for('item_add'))
    return render_template('item_add.html', title='Add new Item', form=form)