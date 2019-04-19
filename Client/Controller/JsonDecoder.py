import json
import threading

from Functions.Upload import Upload

#to decode the message from receiver
class JsonDecoder(threading.Thread):

    def __init__(self,jsons):
        threading.Thread.__init__(self)
        self.jsons = jsons

    def run(self):
            self.Decide()


    def Decide(self):
        jsons = self.jsons
        func = jsons["func"] # this is the most important the functionality of the message

        if(func == "upload_req_success"): # if the upload request has success
            node_ip = jsons["node_ip"] #node ip to send to
            node_port = jsons["node_port"] # node port to send to

            upload = Upload()
            upload.uploadFile(node_ip,node_port) # upload the file

        elif(func == "upload_req_failed"):
            msg = jsons["msg"]
            reason = jsons["reason"]

            upload = Upload()
            upload.uploadError(msg, reason)
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



