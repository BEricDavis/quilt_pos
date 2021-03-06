from app import app, db
from app.models import Customer, Item, User, Purchase

@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'Customer': Customer, 'Item': Item, 'User': User, 'Purchase': Purchase}