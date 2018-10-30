from server import api, application

@application.route('/')
def home():
    return "Welcome to Seefood Server!"
