import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    
class ProductionConfig(Config):
    DEBUG = os.environ.get('DEBUG') or ""
    TESTING = os.environ.get('TESTING') or ""


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    PORT = 5002
    FLASK_APP="app.py"

