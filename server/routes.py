from server import api, application
from ImageResource import Image

@application.route('/')
def home():
    return "Welcome to Seefood Server!"
