from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Customer
from app.forms import NewCustomerForm

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