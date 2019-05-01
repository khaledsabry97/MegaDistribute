import os

from Controller.JsonEncoder import JsonEncoder
from Data.data import Data


class Download:

    def __init__(self):
            pass

    def send_download_request(self,ips,ports): # to the keeper
        Data.no_ports=len(ports)
        Data.path_array=[""]*Data.no_ports
        size = os.path.getsize(Data.currentFilePath) / len(ports)  #size of the chunk
        for x in range(0, len(ports)):
            start_ind = size * (x - 1)
            jsonEncoder=JsonEncoder()
            jsonEncoder.download_req(Data.userId, Data.fileName, Data.ip,ips[x],ports[x],start_ind,size,x)

    def sendDownloadReq(self):     #send to master
        jsonEncoder = JsonEncoder()
        jsonEncoder.downloadReq( Data.userId, Data.fileName, Data.getIp(), Data.getMasterIp(), Data.getMasterPort() )

    def downloadError(self, msg):
        print( msg )
        Data.fileName = input( "what is the name of your file : " )
        self.sendDownloadReq()


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



