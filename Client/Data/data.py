import random
import socket


class Data:

    global currentFilePath,fileName,userId,ip
    currentFilePath  = ""
    fileName = ""
    userId = 1
    ip = " "
    DatabaseSlavesIp = ["1923.295,28895923,295295"]

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
        ip = socket.gethostbyname(socket.gethostname())
        return (socket.getfqdn())


    @staticmethod
    def getDatabaseSlaveIp():
        DatabaseSlavesIp = ["192.168.0.105","192.168.0.106","192.168.0.107"]
        random.shuffle(DatabaseSlavesIp)  # randomize the array of nodes
        return DatabaseSlavesIp

    @staticmethod
    def getDatabaseMaster():
        masterDatabaseIp = "localhost"
        return  masterDatabaseIp


