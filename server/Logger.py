import os
import datetime
class Logger():
    def __init__(self):
        self.filename = str(datetime.datetime.now) + ".log"
        self.filename = os.path.dirname(os.path.abspath(__file__)) + "/logs/" + str(datetime.datetime.now()) + ".log"

    def write_info(self, info):
        file = open(self.filename, "a")
        file.write("({} | INFO): {}\n".format(datetime.datetime.now(), info))
        file.close()
    
    def write_error(self, error):
        file = open(self.filename, "a")
        file.write("({} | ERROR): {}\n".format(datetime.datetime.now(), error))
        file.close()