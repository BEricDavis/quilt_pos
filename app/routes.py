from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Customer, Item
from app.forms import NewCustomerForm, NewItemForm, EditCustomerForm, EditItemForm
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#===================
# Customer routes
#===================
@app.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    form = NewCustomerForm()


    if form.validate_on_submit():
        print('validated')
        customer = Customer(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            birthday=form.birthday.data,
                            street1=form.street1.data,
                            street2=form.street2.data,
                            city=form.city.data,
                            state=form.state.data,
                            zip=form.zip.data
                            )
        db.session.add(customer)
        db.session.commit()
        flash('Customer added')
        return redirect(url_for('customer_edit', customer_id=customer.id))
    else:
        print('not validated')

    return render_template('customer_add.html', title='Add new customer', form=form)

@app.route('/customer/list', methods=['GET'])
def customer_list():
    page = request.args.get('page', 1, type=int)

    customers = Customer.query.order_by(Customer.last_name.asc()).paginate(
        page, app.config['CUSTOMERS_PER_PAGE'], False
    )
    next_url = url_for('customer_list', page=customers.next_num) if customers.has_next else None
    prev_url = url_for('customer_list', page=customers.prev_num) if customers.has_prev else None

    return render_template('customer_list.html', title='Customer List', customers=customers.items,
                           next_url=next_url, prev_url=prev_url)

@app.route('/customer/edit/<customer_id>', methods=['GET','POST'])
# TODO: add validation that the email doesn't already exist
def customer_edit(customer_id):

    customer = Customer.query.filter_by(id=customer_id).first()
    # TODO: does adding the object here buy me anything?
    form = EditCustomerForm(obj=customer)
    app.logger.info(customer)
    if customer is None:
        flash('Customer not found')
        return render_template('customer_list.html')

    if customer.birthday is None:
        app.logger.info('Updating birthday')
        customer.birthday=app.config['DATEUTIL_DEFAULT']
        db.session.commit()

    elif form.validate_on_submit():
        customer.first_name = form.first_name.data
        customer.last_name = form.last_name.data
        customer.email = form.email.data
        customer.birthday = datetime(form.birthday.data.year, form.birthday.data.month, form.birthday.data.day)
        customer.street1 = form.street1.data
        customer.street2 = form.street2.data
        customer.city = form.city.data
        customer.state = form.state.data
        customer.zip = form.zip.data

        db.session.commit()
        flash('Customer updated')

        return redirect(url_for('customer_edit', customer_id=customer.id))

    elif request.method == 'GET':
        form.first_name.data = customer.first_name
        form.last_name.data = customer.last_name
        form.email.data = customer.email
        form.birthday.data = customer.birthday
        print(type(form.birthday.data))
        #form.birthday = customer.birthday.strftime('%m/%d')
        # form.birthday = datetime.strptime(customer.birthday, app.config['DATEUTIL_DEFAULT'])
        form.street1.data = customer.street1
        form.street2.data = customer.street2
        form.city.data = customer.city
        form.state.data = customer.state
        form.zip.data = customer.zip

    return render_template('customer_add.html', title='Edit Customer', form=form)


#================
# Item routes
#================
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

@app.route('/item/list', methods=['GET'])
def item_list():
    page = request.args.get('page', 1, type=int)

    items = Item.query.order_by(Item.description.asc()).paginate(
        page, app.config['ITEMS_PER_PAGE'], False
    )
    next_url = url_for('item_list', page=items.next_num) if items.has_next else None
    prev_url = url_for('item_list', page=items.prev_num) if items.has_prev else None

    return render_template('item_list.html', title='Item List', items=items.items,
                           next_url=next_url, prev_url=prev_url)

@app.route('/item/edit/<id>', methods=['GET', 'POST'])
def item_edit(id):
    item = Item.query.filter_by(id=id).first()
    form = EditItemForm(obj=item)


    if form.validate_on_submit():
        item.description = form.description.data
        item.sku = form.sku.data
        item.item_number = form.item_number.data
        item.quantity = form.quantity.data
        item.cost = form.cost.data
        item.price = form.price.data


        db.session.commit()
        flash('Item updated')
        return redirect(url_for('item_edit', id=id))

    elif request.method == 'GET':
        return render_template('item_add.html', title='Edit Item', form=form)