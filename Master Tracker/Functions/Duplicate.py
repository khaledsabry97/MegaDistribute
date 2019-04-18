import threading

import time

from Connections.DataBaseController import DatabaseController
from Data.Datakeepers import DataKeepers
from Controller.JsonEncoder import JsonEncoder


class Duplicate(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            self.checkPeriodic()
            time.sleep(2)


    #check periodic if file not in 3 data nodes
    def checkPeriodic(self):
        array = DatabaseController.getLessThan3Duplication()
        userIdMap = {}

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
            userIdMap[userId][fileName].append(int(nodeId))

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
                senderNodeId = int(senderNodeId)
                senderIp = DataKeepers.getDataNodeIp(senderNodeId)
                senderPort = DataKeepers.getRandomPort(senderNodeId)
                newNodeIdList,_= DataKeepers.getAliveDataNodesExclude(nodeIds)
                for k in range(len(newNodeIdList)):
                    receiverNodeId = newNodeIdList[k]
                    receiverIp = DataKeepers.getDataNodeIp(receiverNodeId)
                    receiverPort = DataKeepers.getRandomPort(receiverNodeId)
                    jsonGenerator = JsonEncoder()
                    jsonGenerator.duplicate(currentUserId,currentFileName,senderIp,senderPort,receiverIp,receiverPort)
                    DatabaseController.addDuplicateNoSuccess(currentUserId,receiverNodeId,currentFileName)

        DatabaseController.deleteDuplicateMoreThan6HoursNoSuccess()


    def duplicateComplete(self,userId,fileName,fileSize,nodeId):
        DatabaseController.updateDuplication(userId,nodeId,fileName)






