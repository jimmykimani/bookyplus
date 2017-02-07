#!/usr/bin/env python
import os 
from flask_script import Manager, prompt_bool
from thermo import app, db
from thermo.models import User

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="jimmy", email="jimmykkimani@gmail.com"))
    db.session.add(User(username="joan", email="joan@gmail.com"))
    db.session.commit()
    print 'intialized the database'

@manager.command
def dropdb():
    if prompt_bool(
        'Are you sure?'):
        db.drop_all()
        print 'haha dropped em all'
        
if __name__ == '__main__':
    manager.run()