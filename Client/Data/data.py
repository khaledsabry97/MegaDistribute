import random
import socket


class Data:

    global currentFilePath,fileName,userId,ip,path_array,files_recieved,file_size
    currentFilePath  = ""
    fileName = ""
    file_size=0
    userId = 1
    ip = " "
    path_array=[""]*6
    files_recieved=False

    #DatabaseSlavesIp = ["1923.295,28895923,295295"]

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
    def getIp():
        ip = socket.gethostbyname(socket.gethostname())
        #return (socket.getfqdn())
        return "localhost"


    @staticmethod
    def getDatabaseSlaveIp():
        DatabaseSlavesIp = ["192.168.137.36","192.168.43.34","192.168.43.153"]
        random.shuffle(DatabaseSlavesIp)  # randomize the array of nodes
        return DatabaseSlavesIp

    @staticmethod
    def getDatabaseMaster():
        masterDatabaseIp = "192.168.137.50"
        return  masterDatabaseIp


