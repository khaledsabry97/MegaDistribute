import os

from Connections.ReceiverController import ReceiverController
from Controller.JsonEncoder import JsonEncoder
from Data import data
from Data.data import Data
from Functions.FileSystem import FileSystem


class Download:

    def __init__(self):
            pass

    def send_download_request(self,ips,ports):
        Data.no_ports=len(ports)
        Data.path_array=[""]*Data.no_ports
        size = os.path.getsize(Data.currentFilePath) / len(ports)  #size of the chunk
        for x in range(0, len(ports)):
            start_ind = size * (x - 1)
            jsonEncoder=JsonEncoder()
            jsonEncoder.download_req(Data.userId, Data.fileName, Data.ip,ips[x],ports[x],start_ind,size,x)



    def check(self):

       for x in range(0,len(Data.path_array)):
           if Data.path_array[x]=="" :
               return 0

       Complete_video = open("Complete video.mp4", "w")
       for Part in Data.path_array:
           video= open(Part, "r")
           Complete_video.write(video.read())
           video.close()

       Complete_video.close()



