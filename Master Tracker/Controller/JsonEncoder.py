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
        func = "duplicate"
        sendingMsg = {"func":func,
                      "user_id":userId,
                      "file_name":fileName,
                      "receiver_ip":receiverNodeIp,
                      "receiver_port":recieverNodePort}

        jsons = json.dumps(sendingMsg)
        self.send(senderNodeIp,senderNodePort,jsons)


