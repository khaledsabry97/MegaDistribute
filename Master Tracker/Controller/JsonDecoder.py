import json
import threading

from Functions import Upload, Duplicate, Download


class JsonDecoder(threading.Thread):

    def __init__(self,jsons):
        threading.Thread.__init__(self)
        self.jsons = jsons

    def run(self):
            self.Decide()


    def Decide(self):
        jsons = self.jsons
        func = jsons["func"]

        if(func == "upload_request"):
            user_id = jsons["user_id"]
            file_name = jsons["file_name"]
            client_ip = jsons["client_ip"]

            upload = Upload()
            upload.uploadRequest(user_id,file_name,client_ip)

        elif(func == "upload_complete"):
            user_id = jsons["user_id"]
            file_size = jsons["file_size"]
            file_name= jsons["file_name"]
            node_id= jsons["node_id"]

            upload = Upload()
            upload.uploadComplete(user_id,file_name,file_size,node_id)

        elif(func =="duplicate_complete"):
            user_id = jsons["user_id"]
            file_size = jsons["file_size"]
            file_name = jsons["file_name"]
            node_id = jsons["node_id"]
            duplicate = Duplicate()
            duplicate.duplicateComplete(user_id,file_name,file_size,node_id)

        elif (func == "download_request"):
            user_id = jsons["user_id"]
            client_ip = jsons["client_ip"]

            download = Download()
            download.showFiles(user_id,client_ip)

        elif (func == "download_file"):
            user_id = jsons["user_id"]
            file_name = jsons["file_name"]
            client_ip = jsons["client_ip"]
            download = Download()
            download.downloadFile(user_id,file_name,client_ip)


