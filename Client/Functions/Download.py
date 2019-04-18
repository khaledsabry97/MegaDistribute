from Connections.DataBaseController import DatabaseController
from Controller import JsonEncoder
from Data.Datakeepers import DataKeepers


class Download:
    def __init__(self):
        pass


    def showFiles(self,userId,receiverIp):
        arr = DatabaseController.getFiles(userId)

        file_Names = []
        fileSize = []
        for i in range(len(arr)):
            file_Names.append(arr[i]["file_name"])
            fileSize.append(arr[i]["file_size"])


        jsonEncoder = JsonEncoder()
        jsonEncoder.showFiles(file_Names,fileSize,receiverIp)



    def downloadFile(self,userId,fileName,clientIp):
        arr = DatabaseController.getNodesContainsFile(userId,fileName)


        structure = {}
        for i in range(len(arr)):
            nodeId = arr[i]["node_id"]
            file_Name = arr[i]["file_name"]

            if file_Name not in structure:
                structure[file_Name] = []
            structure[file_Name].append(nodeId)

        if fileName in structure:
            ips,ports,_,_ = DataKeepers.getIpsandPorts(structure[file_Name])

            jsonEncoder = JsonEncoder()
            jsonEncoder.downloadIpsPorts(ips, ports, clientIp)

        else:
            self.incorrectFileName(fileName,clientIp)

    def incorrectFileName(self, fileName, clientIp):
        msg = "you have no file with this name: "+fileName

        jsonEncoder = JsonEncoder()
        jsonEncoder.downloadReqFailed(msg, fileName, clientIp)
