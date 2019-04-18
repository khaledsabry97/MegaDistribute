import base64
import threading
import json
import zmq
import time
import sys

import requests

class por(threading.Thread):
    id = "1"
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.sendPeriodic()


    def sendPeriodic(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:%s" % 3000)
        
        while True:
            #  Wait for next request from client
            message = socket.recv_json()
            type(message)
            jsons = json.loads(message)
            part = jsons["part"]
            video = jsons["video"]
            c = video.encode('ascii')
            c = base64.decodebytes(c)
            with open("["+str(jsons["user_id"])+"] test.mp4", "ab") as binary_file:
                # Write text or bytes to the file
                num_bytes_written = binary_file.write(c)

            print("Part" + str(part))
            socket.send_json(message)
