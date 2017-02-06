#!/usr/bin/env python
import os
from flask_script import Manager, Shell, prompt_bool
from thermos import app, db

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    print 'intialized the database'

@manager.command
def dropdb():
    if prompt_bool(
        'Are you sure?'):
        db.drop_all()
        print 'haha dropped em all'
        
if __name__ == '__main__':
    manager.run()