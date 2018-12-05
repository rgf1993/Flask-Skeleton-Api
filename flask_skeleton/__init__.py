from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
import logging

# from mindmap_api import Config
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flask_skeleton import models

from flask_skeleton import views