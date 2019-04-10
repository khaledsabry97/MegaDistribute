import threading
import time
import requests

from DatabaseBackupServer.InsertThread import InsertThread
from DatabaseBackupServer.links import Links


class BackupThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.checkBackup()

    def checkBackup(self):

        while (True):
            try:
                r = requests.post(url=Links.checkBackupRequest, data={})
                print(r.text)
                result = r.json()
                if (result["server_response"] != "server down" and result["server_response"] != False):
                    self.insertBackUp(result["server_response"]);
            except:
                pass

            time.sleep(3)

    def insertBackUp(self, json):
        dict = {}
        size = len(json)
        for i in range(size):
            if json[i]["server_id"] not in dict:
                dict[json[i]["server_id"]] = []

            dict[json[i]["server_id"]].append(json[i])

        array = list(dict.keys())
        for i in range (len(array)):
            thread = InsertThread(dict[array[i]], array[i])
            thread.start()
