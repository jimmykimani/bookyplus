from flask_bootstrap import Bootstrap
from flask import Flask



bootstrap = Bootstrap()




def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)
    return app 