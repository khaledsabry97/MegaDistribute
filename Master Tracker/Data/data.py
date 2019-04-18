import random


class Data:

    def __init__(self):
        self.masterIp = ""
        self.masterPorts = [6000,6002,6004]


    def getMasterIp(self):
        return self.masterIp

    def getMasterPort(self):
        random.shuffle(self.masterPorts)  # randomize the array of nodes
        return self.masterPorts[0]