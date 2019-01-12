from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return '<html><h1>Welcome to the Little Shop of Stitches!</h1></html>'

