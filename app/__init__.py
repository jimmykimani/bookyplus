import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config
# from models import User, Bookmark,Tag



moment = Moment()
db = SQLAlchemy()
bootstrap = Bootstrap()
# bootstrap.init_app(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
# login_manager.init_app(app)



def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)


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

 

    return app
    # import models
    # import ..views

