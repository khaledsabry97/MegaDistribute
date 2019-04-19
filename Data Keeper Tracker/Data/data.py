import random


class Data:

    def __init__(self):
        self.ip = ""
        self.masterIp = ""
        self.masterPorts = [10000,6002,6004]
        self.id = 2


    def getMasterIp(self):
        return self.masterIp

    def getMasterPort(self):
        random.shuffle(self.masterPorts)  # randomize the array of nodes
        return self.masterPorts[0]

    def getLocalIp(self):
        return self.ip

    def getId(self):
        return self.id
