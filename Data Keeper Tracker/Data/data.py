import random
import socket


class Data:

    global id
    id = 1
    def __init__(self):
        pass

    @staticmethod
    def getMasterIp():
        masterIp = "192.168.137.50"
        return masterIp

    @staticmethod
    def getMasterPort():
        masterPorts = [10000, 10002, 10004]
        random.shuffle(masterPorts)  # randomize the array of nodes
        return masterPorts[0]

    @staticmethod
    def getLocalIp(self):
        # return (socket.getfqdn())
        return "192.168.137.36"
