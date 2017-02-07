#!/usr/bin/env python
import os 
from flask_script import Manager, prompt_bool
from thermo import app, db
from thermo.models import User, Bookmark, Tag
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    db.create_all()
    db.session.add(User(username="jimmy", email="jimmykkimani@gmail.com", password='test'))
    db.session.add(User(username="joan", email="joan@gmail.com", password='test'))
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