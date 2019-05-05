import os

from Controller.JsonEncoder import JsonEncoder
from Data.data import Data
from Functions.Download import Download


class Show () :



    def __init__(self):
            pass




    def snd_shw_req(self): #to master

      jsonEncoder = JsonEncoder()
      jsonEncoder.showReq( Data.userId, Data.getIp(), Data.getMasterIp(), Data.getMasterPort())


    def gt_req_fname(self,files,fileSizes) :  # to master
        if len(files)==0 :
            print ("u have no files")
            Data.fileName=""  # user has no files
        else :

          for i in range ( len ( files ) ) :
             print(str(i)+" )  "+ str(files[i]))
          while True :
           file_number = input ( "enter the number of the file " )

           if  0 <= int(file_number ) < len(files)  :
               # call the download class
               Data.fileName = files[int(file_number)]
               Data.file_size=fileSizes[int(file_number)]

               print("downloading")
               download = Download ()
               download.sendDownloadReq ()
               break

           else :
                print("wrong number ")









