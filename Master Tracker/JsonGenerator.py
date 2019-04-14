import json

from SenderController import SenderController


class JsonGenerator:

    def __init__(self):
       pass

    def duplicate(self,userId,fileName,senderNodeIp,senderNodePort,receiverNodeIp,recieverNodePort):
        func = "duplicate"
        sendingMsg = {"func":func,
                      "user_id":userId,
                      "file_name":fileName,
                      "receiver_ip":receiverNodeIp,
                      "receiver_port":recieverNodePort}

        jsons = json.dumps(sendingMsg)
        thread = SenderController(senderNodeIp,senderNodePort,jsons)
        thread.start()


