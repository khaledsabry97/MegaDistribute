import base64
import os
import threading

import zmq
import time
import sys
import codecs
import requests
import json


class Read(threading.Thread):
    id = "1"
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.sendPeriodic()


    def sendPeriodic(self):
        context = zmq.Context()

        "Connecting to server..."
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:%s" % 3000)



