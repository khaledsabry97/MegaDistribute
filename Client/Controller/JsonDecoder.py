import json
import threading

from Functions.Download import Download
from Functions.FileSystem import FileSystem
from Functions.Show import Show
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

        elif (func == "download_req_failed"):
            msg = jsons["msg"]
            reason = jsons["reason"]

            download = Download()
            download.downloadError( msg, reason )




        elif(func=="download_ips_ports"):   #comes from master then send request to keepers
            ips=jsons["ips"]
            ports=jsons["ports"]
            download=Download()
            download.send_download_request(ips,ports)

        elif (func == "show_files"):  # comes from master then send request to keepers
            files = jsons["files"]
            fileSizes = jsons["fileSizes"]
            show =Show()
            show.gt_req_fname(files,fileSizes)


        elif (func=="downloading_part")    :  #download parts from keepers
           user_id=jsons["user_id"]
           file_name=jsons["file_name"]
           current_size=jsons[ "current_size"]
           video=jsons["video"]
           current_part=jsons[ "current_part"]

           fileSystem = FileSystem()
           fileSystem.write_part(current_size, video, user_id, file_name,current_part)
           download = Download()
           download.check()














