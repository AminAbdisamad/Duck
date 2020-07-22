

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from duckApp.config import Config


app = Flask(__name__)
# Configs
app.config.from_object(Config)

# DB initiation
db = SQLAlchemy(app)
# Flask Migration
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
# To get a nice message - Please log in to access this page.
loginManager.login_view = "login"
loginManager.login_message_category = "info"

from duckApp import routes
