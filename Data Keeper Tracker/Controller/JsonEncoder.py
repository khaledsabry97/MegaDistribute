import base64
import json
import os

from Connections.SenderController import SenderController
from Data.data import Data


class JsonEncoder:

    def __init__(self):
       pass


    def send(self,ip,port,json):
        thread = SenderController(ip,port,json)
        thread.run()


    def uploadCompleted(self,user_id,file_name,file_size,node_id,receiverIp,receiverPort):
        func = "upload_complete"
        sendingMsg = {"func": func,
                      "user_id": user_id,
                      "file_name": file_name,
                      "file_size": file_size,
                      "node_id": node_id}

        jsons = json.dumps(sendingMsg)
        self.send(receiverIp, receiverPort, jsons)

    def duplicateCompleted(self, user_id, file_name, file_size, node_id, receiverIp, receiverPort):
        func = "duplicate_complete"
        sendingMsg = {"func": func,
                      "user_id": user_id,
                      "file_name": file_name,
                      "file_size": file_size,
                      "node_id": node_id}

        jsons = json.dumps(sendingMsg)
        self.send(receiverIp, receiverPort, jsons)

    def duplicateVideo(self,user_id,file_name,receiverIp,receiverPort):
        currentPath = "./" + str(Data.id) + "/" + "[" + str(user_id) + "] " + file_name + ".mp4"
        with open(currentPath, "rb") as binary_file:
            # Seek a specific position in the file and read N bytes
            byte = 0
            bytesToRead = 1024 *1024
            size = os.path.getsize(currentPath)
            while(byte < size):
                    binary_file.seek(0, 1)  # Go to beginning of the file
                    couple_bytes = binary_file.read(bytesToRead)
                    #print(couple_bytes)

                    c = base64.encodebytes(couple_bytes)
                    c = c.decode('ascii')
                    func = "duplicate"
                    sendingMsg = {"func": func,
                                  "user_id": user_id,
                                  "file_name": file_name,
                                  "current_size": byte,
                                  "video":c
                                  }

                    jsons = json.dumps(sendingMsg)
                    self.send(receiverIp, receiverPort, jsons)
                    byte +=bytesToRead
        func = "duplicate_complete"
        sendingMsg = {"func": func,
                      "user_id": user_id,
                      "file_name": file_name,
                      "file_size": size
                      }

        jsons = json.dumps(sendingMsg)
        self.send(receiverIp, receiverPort, jsons)
    def uploadCompleted(self,user_id,file_name,file_size,node_id,receiverIp,receiverPort):
        func = "upload_complete"
        sendingMsg = {"func": func,
                      "user_id": user_id,
                      "file_name": file_name,
                      "file_size": file_size,
                      "node_id": node_id}

        jsons = json.dumps(sendingMsg)
        self.send(receiverIp, receiverPort, jsons)



