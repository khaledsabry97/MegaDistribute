import threading
import time
import requests

from DatabaseBackupServer.InsertThread import InsertThread
from DatabaseBackupServer.links import Links

#to check and insert the indices from backup database to slaves databases
class BackupThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.checkBackup()

# check the backup database to get all the indices in the backup
    def checkBackup(self):

        while (True):
            try:
                r = requests.post(url=Links.checkBackupRequest, data={})
                result = r.json()

                if (result["server_response"] != "server down" and result["server_response"] != False):
                    array = result["server_response"]
                    print("Found " + str(len(array)) + ": " + r.text)
                    self.insertBackUp(array);
            except:
                print("BackupThread-checkbackup")

            time.sleep(3)

    #if found something insert it to the slaves databases
    def insertBackUp(self, json):

        #here we trying to collect all the indices to its database slave server id
        dict = {}
        size = len(json)
        for i in range(size):
            if json[i]["server_id"] not in dict:
                dict[json[i]["server_id"]] = []

            dict[json[i]["server_id"]].append(json[i])

        #we loop on all the server ids to add to them their indices
        array = list(dict.keys())
        for i in range (len(array)):
            thread = InsertThread(dict[array[i]], array[i]) #open another thread
            thread.start()
