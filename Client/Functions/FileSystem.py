import base64
import os
import threading

import zmq
import time
import sys

import requests

from Data.data import Data



class FileSystem:
    def __init__(self):
        pass

    def write_part(self,current_size,video,user_id,file_name,part_number):
        c = video.encode('ascii')
        c = base64.decodebytes(c)
        currentPath = "./"+str(Data.id)+"/"+"[" + str(user_id) + "] "+file_name+str(part_number)+".mp4"
        Data.path_array[part_number]=currentPath
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


