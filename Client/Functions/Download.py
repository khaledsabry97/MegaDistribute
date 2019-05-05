import os

from Controller.JsonEncoder import JsonEncoder
from Data.data import Data



class Download:

    def __init__(self):
            pass

    def send_download_request(self,ips,ports): # to the keeper
        Data.no_ports=len(ports)
        Data.path_array=[""]*Data.no_ports
        size = int(int(Data.file_size )/ len(ports) ) #size of the chunk

        for x in range(1, (Data.no_ports+1)):
            start_ind = size * (x - 1)
            if x == Data.no_ports :
               size =size+ int(Data.file_size )% len(ports)

            jsonEncoder=JsonEncoder()
            jsonEncoder.download_req(Data.userId, Data.fileName, Data.getIp(),ips[x-1],ports[x-1],start_ind,size,x)

    def sendDownloadReq(self):     #send to master
        jsonEncoder = JsonEncoder()
        jsonEncoder.downloadReq( Data.userId, Data.fileName, Data.getIp(), Data.getMasterIp(), Data.getMasterPort() )

    def downloadError(self, msg):
        print( msg )
        from IO import IO
        IO.functions()


    def check(self):

       for x in range(0,len(Data.path_array)):
           if Data.path_array[x]=="" :
               return 0

       Complete_video = open(Data.fileName+".mp4", "wb+")
       for Part in Data.path_array:
           video= open(Part, "rb+")
           Complete_video.write(video.read())
           video.close()
       for Part in Data.path_array :
           os.remove(Part)
       Complete_video.close()
       print("Download Complete ")
       from IO import IO
       IO.functions()



