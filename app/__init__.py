import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
# from models import User, Bookmark,Tag

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) 


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.sqlite')
db = SQLAlchemy(app)
app.config['DEBUG']= True


bootstrap = Bootstrap()
bootstrap.init_app(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

moment = Moment(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

from .bookmark import bookmark as bookmark_blueprint
app.register_blueprint(bookmark_blueprint, url_prefix='/bookmark')

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500

 


import models
# import ..views

