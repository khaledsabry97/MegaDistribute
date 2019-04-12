import threading

import zmq
import time
import sys

import requests

class PublisherLive(threading.Thread):
    id = "1"
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.sendPeriodic()


    def sendPeriodic(self):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:7001")
        while True:
            messagedata = id
            print("100")
            socket.send_string("1")
            time.sleep(1)
