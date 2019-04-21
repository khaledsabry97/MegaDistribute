import random
import socket


class Data:

    global currentFilePath,fileName,userId,ip,path_array,no_ports
    currentFilePath  = ""
    fileName = ""
    path_array = [""]*6
    userId = 1
    ip = " "
    no_ports=0

    def __init__(self):
     pass

    @staticmethod
    def getMasterIp():
        masterIp = "localhost"
        return masterIp

    @staticmethod
    def getMasterPort():
        masterPorts = [10000, 10002, 10004]
        random.shuffle(masterPorts)  # randomize the array of nodes
        return masterPorts[0]

    @staticmethod
    def getIp():
        return (socket.getfqdn())

