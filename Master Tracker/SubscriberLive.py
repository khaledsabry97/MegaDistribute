import threading

import zmq
import time
import sys

import requests

class SubscriberLive(threading.Thread):
    ips = ["localhost:7001"]
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.sub()


    def sub(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)

        for i in range(len(self.ips)):
         socket.connect("tcp://"+self.ips[i] )
         socket.setsockopt_string(zmq.SUBSCRIBE, str(i + 1))

        for i in range(len(self.ips)):
            strs = str(i)

        while(True):
            s = socket.recv_string()
            print(s)

