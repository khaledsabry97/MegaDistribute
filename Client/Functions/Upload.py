import base64
import json
import os

from Controller.JsonEncoder import JsonEncoder
from Data.data import Data


class Upload:
    def __init__(self):
        pass


    def uploadFile(self,nodeIp,nodePort):    #to the keeper

        currentPath = Data.currentFilePath # ge the path of the file
        fileName = Data.fileName # get name of it
        with open(currentPath, "rb") as binary_file:
            # Seek a specific position in the file and read N bytes
            byte = 0
            bytesToRead = 1024 * 1024 # send by 1 mb chunks
            size = os.path.getsize(currentPath)
            print("uploading....")
            while (byte < size):
                binary_file.seek(0, 1)  # Go to beginning of the file
                couple_bytes = binary_file.read(bytesToRead)
                c = base64.encodebytes(couple_bytes)
                c = c.decode('ascii')

                jsonEncoder = JsonEncoder()
                result = jsonEncoder.upload(Data.userId,fileName,c,byte,nodeIp,nodePort) #upload the chunk
                if(result == "failed"):
                    print("Upload Failed")
                    return
                byte += bytesToRead
            print("upload_complete")
            jsonEncoder = JsonEncoder()
            jsonEncoder.uploadComplete(Data.userId, fileName, size, nodeIp, nodePort)


    def sendUploadReq(self):   # to the master
        jsonEncoder = JsonEncoder()
        jsonEncoder.uploadReq(Data.userId,Data.fileName,Data.getIp(),Data.getMasterIp(),Data.getMasterPort())


    def uploadError(self, msg,reason):
        print(msg)
        if(reason == "Data Nodes"):
            pass
        elif(reason == "Found Same Filename"):
            Data.fileName = input("what is the name of your file : ")
            self.sendUploadReq()

