from Connections.DataBaseController import DatabaseController
from Controller import JsonEncoder
from Data.Datakeepers import DataKeepers


class Upload:
    def __init__(self, userId, fileName, clientIp):
        self.userId = userId
        self.fileName = fileName
        self.clientIp = clientIp

    def uploadRequest(self,user_id,fileName,clientIp):
        #check first if user has a file with this name

        arr = DatabaseController.getFiles(user_id)


        structure = {}
        files = []
        nodes = []
        for i in range(len(arr)):
            nodeId = arr[i]["node_id"]
            file_Name = arr[i]["file_name"]

            if file_Name not in structure:
                structure[file_Name] = []
            structure[file_Name].append(nodeId)

        if fileName in structure:
            self.changeUserName(fileName)
        else:
            id = DataKeepers.getAliveDataNodesExclude()
            ip = DataKeepers.getDataNodeIp(id)
            port = DataKeepers.getRandomPort(id)

            jsonEncoder = JsonEncoder()
            jsonEncoder.uploadReqSuccess(ip, port, clientIp)




    def changeUserName(self,fileName):
        msg = "you have the same file name in the directory, please change your file name"
        jsonEncoder = JsonEncoder()
        jsonEncoder.uploadReqSuccess(msg, fileName, self.clientIp)


    def uploadComplete(self,user_id,file_name,fileSize,nodeId):
        DatabaseController.addFile(self.userId,self.nodeId,self.fileName,fileSize)
