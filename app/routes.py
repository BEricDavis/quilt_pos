from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Customer, Item
from app.forms import NewCustomerForm, NewItemForm

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