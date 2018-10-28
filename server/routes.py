from server import api, app

@app.route('/')
def home():
    return "Welcome to Seefood Server!"
