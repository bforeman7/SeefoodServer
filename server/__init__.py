from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from Logger import Logger

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
application.config['JSON_SORT_KEYS'] = False

database = SQLAlchemy(application)
logger = Logger()

from server import routes
import os

## Do not remove this piece, it is very important. Python scripts will not run correcly
## (i.e. cannot find files for scripts, modules, etc. ) unless you are in cd'ed into the 
## directory which they live in. We have to cd into seefood directory to run the AI's scripts.

# We will change these to be the pwd of where these live out on the server. For debugging purposes change these
# to where your seefood AI dirctory lives (ex. do "pwd" in your seefood directory and copy paste that)
os.chdir("/home/natedunn/Desktop/SeefoodServer/server/seefood")
# this is here for debugging purposes to tell us whether we got to the seefood directory or not
print(os.listdir("/home/natedunn/Desktop/SeefoodServer/server/seefood"))
logger.write_info(os.listdir("/home/natedunn/Desktop/SeefoodServer/server/seefood"))

from seefoodWrapper import SeefoodWrapper

seefoodWrapper = SeefoodWrapper()
database.init_app(application)
database.create_all()