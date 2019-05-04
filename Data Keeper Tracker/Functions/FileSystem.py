import base64
import os
import threading

import zmq
import time
import sys



from Data.data import Data


class FileSystem:
    def __init__(self):
        pass
    def write(self,current_size,video,user_id,file_name):
        c = video.encode('ascii')
        c = base64.decodebytes(c)
        currentPath = "./"+str(Data.id)+"/"+"[" + str(user_id) + "] "+file_name+".mp4"
        mode = "ab"
        if (not os.path.exists(str(Data.id))):
            os.makedirs(str(Data.id))


        if(os.path.exists(currentPath)):
            size = os.path.getsize(currentPath)
            if size != current_size:
                print(str(size) + " : "+str(current_size))
                mode = "wb"



        with open(currentPath, mode) as binary_file:
            binary_file.write(c)

