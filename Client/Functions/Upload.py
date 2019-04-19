import base64
import json
import os

from Controller.JsonEncoder import JsonEncoder
from Data.data import Data


class Upload:
    def __init__(self):
        pass


    def uploadFile(self,nodeIp,nodePort):
        currentPath = Data.currentFilePath
        fileName = Data.fileName
        with open(currentPath, "rb") as binary_file:
            # Seek a specific position in the file and read N bytes
            byte = 0
            bytesToRead = 1024 * 1024
            size = os.path.getsize(currentPath)
            print("uploading....")
            while (byte < size):
                binary_file.seek(0, 1)  # Go to beginning of the file
                couple_bytes = binary_file.read(bytesToRead)
                # print(couple_bytes)

                c = base64.encodebytes(couple_bytes)
                c = c.decode('ascii')
                jsonEncoder = JsonEncoder()
                jsonEncoder.upload(Data.userId,fileName,c,byte,nodeIp,nodePort)
                byte += bytesToRead
            print("upload_complete")
            jsonEncoder = JsonEncoder()
            jsonEncoder.uploadComplete(Data.userId, fileName, size, nodeIp, nodePort)


    def sendUploadReq(self):
        jsonEncoder = JsonEncoder()
        jsonEncoder.uploadReq(Data.userId,Data.fileName,Data.getIp(),Data.getMasterIp(),Data.getMasterPort())


    def changeFileName(self,msg):
        print(msg)
        Data.fileName = input("what is the name of your file : ")
        self.sendUploadReq()

