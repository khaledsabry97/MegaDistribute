import threading

import time
import sys

import requests

from DataBaseController import DatabaseController
from Datakeepers import DataKeepers
from JsonGenerator import JsonGenerator


class Duplicate(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            time.sleep(2)
            self.checkPeriodic()



    def checkPeriodic(self):
        json = DatabaseController.getLessThan3Duplication()
        userIdMap = {}

        array = json["server_response"]

        #adding the structure of maps
        for i in range(len(array)):
            userId = array[i]["user_id"]
            nodeId = array[i]["node_id"]
            fileName = array[i]["file_name"]
            if userId not in userIdMap:
                userIdMap[userId] = {}
            fileMap = userIdMap[userId]
            if fileName not in fileMap:
                userIdMap[userId][fileName]= []
            userIdMap[userId][fileName].append(nodeId)

        userIdKeys = list(userIdMap.keys())
        for i in range(len(userIdKeys)):
            currentUserId = userIdKeys[i]
            fileKeys = list(userIdMap[currentUserId].keys())
            for j in range(len(fileKeys)):
                currentFileName = fileKeys[j]
                nodeIds = userIdMap[currentUserId][currentFileName]
                senderNodeId,found = DataKeepers.getNodeIdAliveInclude(nodeIds)
                if found == False:
                    continue

                senderIp = DataKeepers.getDataNodeIp(senderNodeId)
                senderPort = DataKeepers.getRandomPort(senderNodeId)
                newNodeIdList = DataKeepers.getAliveDataNodesExclude(nodeIds)
                for k in range(len(newNodeIdList)):
                    receiverNodeId = newNodeIdList[k]
                    receiverIp = DataKeepers.getDataNodeIp(receiverNodeId)
                    receiverPort = DataKeepers.getRandomPort(receiverNodeId)
                    jsonGenerator = JsonGenerator()
                    jsonGenerator.duplicate(currentUserId,currentFileName,senderIp,senderPort,receiverIp,receiverPort)
                    DatabaseController.addDuplicateNoSuccess(currentUserId,receiverNodeId,currentFileName)

        DatabaseController.deleteDuplicateMoreThanOneDayNoSuccess()









