import os
from dotenv import load_dotenv


load_dotenv()
# Get Database Details from .env file
dbName = os.getenv("DB_NAME")
dbUser = os.getenv("USER_NAME")
dbPassword = os.getenv("PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")


class Config:
    # secret
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # app.config["SECRET_KEY"] = SECRET_KEY
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# DB Configuration
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = f"mysql://{dbUser}:{dbPassword}@localhost/{dbName}"
