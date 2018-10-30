from server import application

#run in development
if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)