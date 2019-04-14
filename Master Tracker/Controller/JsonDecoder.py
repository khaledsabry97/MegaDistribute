import json
import threading

from Connections.SenderController import SenderController


class JsonDecoder(threading.Thread):
    def __init__(self,jsons):
        threading.Thread.__init__(self)
        self.jsons = jsons

    def run(self):
            self.Decide()


    def Decide(self):
        func = self.jsons["func"]
        if(func == "hello"):
            pass


