import base64
import json
import os

from Controller.JsonEncoder import JsonEncoder
from Data.data import Data


class Upload:
    def __init__(self):
        pass


    def uploadFile(self,nodeIp,nodePort):
        data = Data()
        currentPath = data.currentFilePath
        fileName = data.fileName
        with open(currentPath, "rb") as binary_file:
            # Seek a specific position in the file and read N bytes
            byte = 0
            bytesToRead = 1024 * 1024
            size = os.path.getsize(currentPath)
            while (byte < size):
                binary_file.seek(0, 1)  # Go to beginning of the file
                couple_bytes = binary_file.read(bytesToRead)
                # print(couple_bytes)

                c = base64.encodebytes(couple_bytes)
                c = c.decode('ascii')
                jsonEncoder = JsonEncoder()
                jsonEncoder.upload(data.userId,fileName,c,byte,nodeIp,nodePort)
                byte += bytesToRead

            jsonEncoder = JsonEncoder()
            jsonEncoder.uploadComplete(data.userId, fileName, size, nodeIp, nodePort)


    def sendUploadReq(self):
        data = Data()
        jsonEncoder = JsonEncoder()
        jsonEncoder.uploadReq(Data.userId,Data.fileName,data.getIp(),data.getMasterIp(),data.getMasterPort())


    def changeFileName(self,msg):
        print(msg)
        data = Data()
        data.fileName = input("what is the name of your file : ")
        self.sendUploadReq()

