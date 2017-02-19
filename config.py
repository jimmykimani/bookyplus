import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}