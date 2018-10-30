from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 

application = Flask(__name__)
api = Api(application)
database = SQLAlchemy(application)

from server import routes