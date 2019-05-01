import threading
import time

import zmq

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
        link = "tcp://*:"+str(5006+Data.id*1000)
        socket.bind(link)
        while True:
            #print(Data.id)
            socket.send_string(str(Data.id))
            time.sleep(1)
