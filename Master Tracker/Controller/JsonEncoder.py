import json

from Connections.SenderController import SenderController


class JsonEncoder:

    def __init__(self):
       pass


    def send(self,ip,port,json):
        thread = SenderController(ip,port,json)
        thread.start()

    #send duplication request to the data node
    def duplicate(self,userId,fileName,senderNodeIp,senderNodePort,receiverNodeIp,recieverNodePort):
        func = "duplicate_request"
        sendingMsg = {"func":func,
                      "user_id":userId,
                      "file_name":fileName,
                      "receiver_ip":receiverNodeIp,
                      "receiver_port":recieverNodePort}

        jsons = json.dumps(sendingMsg)
        self.send(senderNodeIp,senderNodePort,jsons)


    def uploadReqSuccess(self,nodeIp,nodePort,receiverIp):
        func = "upload_req_success"
        sendingMsg = {"func":func,
                      "node_ip":nodeIp,
                      "node_port":nodePort}

        jsons = json.dumps(sendingMsg)
        self.send(receiverIp,3000,jsons)

    def uploadReqFailed(self,msg,fileName,receiverIp):
        func = "upload_req_failed"
        sendingMsg = {"func":func,
                      "msg":msg,
                      "file_name":fileName}

        jsons = json.dumps(sendingMsg)
        self.send(receiverIp,3000,jsons)


