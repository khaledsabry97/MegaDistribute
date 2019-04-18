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
        with open("adele.mp4", "rb") as binary_file:
            # Seek a specific position in the file and read N bytes
            i = 0
            byte = 0
            bytesToRead = 1024 *1024
            size = os.path.getsize("adele.mp4")
            while(byte < size):
                    i += 1
                    byte +=bytesToRead
                    binary_file.seek(0, 1)  # Go to beginning of the file
                    couple_bytes = binary_file.read(bytesToRead)
                    #print(couple_bytes)

                    c = base64.encodebytes(couple_bytes)
                    c = c.decode('ascii')
                    func = "duplicate"
                    sendingMsg = {"func": func,
                                  "user_id": 1,
                                  "part": i,
                                  "video":c ,
                                  "receiver_port": 3000}

                    jsons = json.dumps(sendingMsg)
                    socket.send_json(jsons)
                    #  Get the reply.
                    message = socket.recv_json()


