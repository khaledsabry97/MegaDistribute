import json
import threading

import zmq


from Controller.JsonDecoder import JsonDecoder


class ReceiverController(threading.Thread):

    def __init__(self,port):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        self.receive()


    def receive(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:%s" % self.port)

        while True:
            try:
                #  Wait for next request from client
                message = socket.recv_json()
                type(message)
                jsons = json.loads(message)
                jsonDecoder = JsonDecoder(jsons)
                jsonDecoder.start()
                socket.send_json({"func":"success"})
            except:
                print("error")


