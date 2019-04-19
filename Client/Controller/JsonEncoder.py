import json

from Connections.SenderController import SenderController


class JsonEncoder:

    def __init__(self):
       pass


    def send(self,ip,port,json):
        thread = SenderController(ip,port,json)
        return thread.run()

    def uploadReq(self,user_id,file_name,client_ip,ip,port):
        func = "upload_request"
        sendingMsg = {"func":func,
                      "user_id":user_id,
                      "file_name":file_name,
                      "client_ip":client_ip}

        jsons = json.dumps(sendingMsg)
        self.send(ip,port,jsons)


    def upload(self,userId,fileName,vid,currentSize,nodeIp,nodePort):
        func = "upload"
        sendingMsg = {"func": func,
                      "user_id": userId,
                      "file_name": fileName,
                      "current_size": currentSize,
                      "video": vid
                      }

        jsons = json.dumps(sendingMsg)
        return self.send(nodeIp, nodePort, jsons)




    def uploadComplete(self,userId,fileName,fileSize,nodeIp,nodePort):
        func = "upload_complete"
        sendingMsg = {"func": func,
                      "user_id": userId,
                      "file_name": fileName,
                      "file_size": fileSize
                      }

        jsons = json.dumps(sendingMsg)
        self.send(nodeIp, nodePort, jsons)
