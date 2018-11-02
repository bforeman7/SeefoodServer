from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 

application = Flask(__name__)
api = Api(application)

## FLASK CONFIGURATIONS
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
    user="postgres",
    passwd="password",
    host="localhost",
    port="5432",
    db="seefood_db")
application.config['SECRET_KEY'] = "23rafsdfafsdfaerq2344q2wefasdt359tergascjfaw34oasdf"

database = SQLAlchemy(application)

from server import routes

database.init_app(application)
database.create_all()