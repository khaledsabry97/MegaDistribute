import base64
import json
import os
import threading

from Functions.FileSystem import FileSystem
from Data.data import Data
from Controller.JsonEncoder import JsonEncoder

class JsonDecoder(threading.Thread):
    def __init__(self,jsons):
        threading.Thread.__init__(self)
        self.jsons = jsons

    def run(self):
            self.Decide()


    def Decide(self):
        jsons = self.jsons
        func = jsons["func"]

        if(func == "upload" or func == "duplicate"):
            current_size = jsons["current_size"]
            video = jsons["video"]
            user_id = jsons["user_id"]
            file_name = jsons["file_name"]

            fileSystem = FileSystem()
            fileSystem.write(current_size,video,user_id,file_name)
        elif(func == "upload_complete"):
            user_id = jsons["user_id"]
            file_size = jsons["file_size"]
            file_name= jsons["file_name"]
            jsonEncoder = JsonEncoder()
            jsonEncoder.uploadCompleted(user_id,file_name,file_size,Data.id,Data.getMasterIp(),Data.getMasterPort())

        elif(func =="duplicate_request"):
            user_id = jsons["user_id"]
            file_name = jsons["file_name"]
            receiverIp = jsons["receiver_ip"]
            receiverPort= jsons["receiver_port"]

            jsonEncoder = JsonEncoder()
            threading.Thread(target=jsonEncoder.duplicateVideo, args=(user_id,file_name,receiverIp,receiverPort)).start()
            #jsonEncoder.duplicateVideo(user_id,file_name,receiverIp,receiverPort)

        elif(func =="duplicate_complete"):
            user_id = jsons["user_id"]
            file_size = jsons["file_size"]
            file_name = jsons["file_name"]

            jsonEncoder = JsonEncoder()
            jsonEncoder.duplicateCompleted(user_id, file_name, file_size, Data.id, Data.getMasterIp(),Data.getMasterPort())

        elif(func=="download_request"):
            user_id = jsons["user_id"]
            file_name = jsons["file_name"]
            receiverIp = jsons["client_ip"]
            receiverPort = 3000
            byte = jsons["start_index"]
            bytesToRead = jsons["chunk_size"]
            current_part=jsons["current_part"]
            jsonEncoder=JsonEncoder()
            jsonEncoder.downloadvideo(user_id,file_name,receiverIp,receiverPort,byte,bytesToRead,current_part)













