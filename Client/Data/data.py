import random
import socket


class Data:

    global currentFilePath,fileName,userId,ip
    currentFilePath  = ""
    fileName = ""
    userId = 1
    ip = " "
    #DatabaseSlavesIp = ["1923.295,28895923,295295"]

    @staticmethod
    def getMasterIp():
        masterIp = "192.168.0.102"
        return masterIp

    @staticmethod
    def getMasterPort():
        masterPorts = [10000, 10002, 10004]
        random.shuffle(masterPorts)  # randomize the array of nodes
        return masterPorts[0]

    @staticmethod
    def getIp():
        ip = socket.gethostbyname(socket.gethostname())
        #return (socket.getfqdn())
        return "192.168.0.102"


    @staticmethod
    def getDatabaseSlaveIp():
        DatabaseSlavesIp = ["192.168.43.201","192.168.43.34","192.168.43.153"]
        random.shuffle(DatabaseSlavesIp)  # randomize the array of nodes
        return DatabaseSlavesIp

    @staticmethod
    def getDatabaseMaster():
        masterDatabaseIp = "192.168.0.102"
        return  masterDatabaseIp


