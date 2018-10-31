from server import application

if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    
    http_server = WSGIServer(('', 8000), application)
    http_server.serve_forever()