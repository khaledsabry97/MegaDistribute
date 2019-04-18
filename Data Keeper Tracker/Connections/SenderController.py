import threading

import zmq
import time
import sys

import requests

from Controller.JsonDecoder import JsonDecoder


class SenderController(threading.Thread):

    def __init__(self,ip,port,json):
        threading.Thread.__init__(self)
        self.ip =ip
        self.port = port
        self.json = json

    def run(self):
        self.send()


    def sender(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        link = "tcp://"+self.ip+":"+self.port
        socket.connect(link)
        socket.setsockopt

        socket.send_json(self.json)
        jsons = socket.recv_json()
        thread = JsonDecoder(jsons)
        thread.start()


