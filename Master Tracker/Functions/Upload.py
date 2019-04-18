from Connections.DataBaseController import DatabaseController
from Controller import JsonEncoder
from Data.Datakeepers import DataKeepers


class Upload:
    def __init__(self):
        pass

    def uploadRequest(self,user_id,fileName,clientIp):
        arr = DatabaseController.getFiles(user_id)


        structure = {}
        for i in range(len(arr)):
            nodeId = arr[i]["node_id"]
            file_Name = arr[i]["file_name"]

            if file_Name not in structure:
                structure[file_Name] = []
            structure[file_Name].append(nodeId)

        if fileName in structure:
            self.changeUserName(fileName,clientIp)
        else:
            id = DataKeepers.getAliveDataNodesExclude()
            ip = DataKeepers.getDataNodeIp(id)
            port = DataKeepers.getRandomPort(id)

            jsonEncoder = JsonEncoder()
            jsonEncoder.uploadReqSuccess(ip, port, clientIp)




    def changeUserName(self,fileName,clientIp):
        msg = "you have the same file name in the directory, please change your file name"
        jsonEncoder = JsonEncoder()
        jsonEncoder.uploadReqSuccess(msg, fileName, clientIp)


    def uploadComplete(self,user_id,file_name,fileSize,nodeId):
        DatabaseController.addFile(user_id,nodeId,file_name,fileSize)