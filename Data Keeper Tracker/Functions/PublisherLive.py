import threading

import zmq
import time
import sys

import requests

from Data.data import Data


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
            data = Data()
            socket.send_string(str(data.getId()))
            time.sleep(1)
