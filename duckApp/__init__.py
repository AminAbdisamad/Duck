import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

# Get Database Details from .env file
dbName = os.getenv("DB_NAME")
dbUser = os.getenv("USER_NAME")
dbPassword = os.getenv("PASSWORD")

# secret
SECRET_KEY = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = SECRET_KEY
# DB Configuration
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = f"mysql://{dbUser}:{dbPassword}@localhost/{dbName}"
app.config[
    "SQLALCHEMY_DATABASE_URI"
]=f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
