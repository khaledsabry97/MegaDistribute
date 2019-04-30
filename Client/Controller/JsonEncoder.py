import json
import os

from Connections.SenderController import SenderController
from Data import data


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

    def download_req(self, user_id, file_name, client_ip,ip,port,start_ind,size,current_part):# download request to keeper
        func = "download_request"
        sendingMsg = {"func": func,
                      "user_id": user_id,
                      "file_name": file_name,
                      "client_ip": client_ip,
                      "start_index":start_ind,
                      "chunk_size":size,
                      "current_part":current_part}

        jsons = json.dumps(sendingMsg)
        self.send(ip, port, jsons)

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


    def download_file(self,user_id,file_name,client_ip,ip,port): # request for downloading sent to Master
        func = "download_file"
        sendingMsg = {"func":func,
                      "user_id":user_id,
                      "file_name":file_name,
                      "client_ip":client_ip}

        jsons = json.dumps(sendingMsg)
        self.send(ip,port,jsons)

