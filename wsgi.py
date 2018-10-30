from server import application

## run in production... served with gunicorn, wsgi and nginx
if __name__ == "__main__":
    application.run()