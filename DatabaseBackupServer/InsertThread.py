import threading
import requests

from links import Links

#to check connectivity to specific slave database server and insert in the database what was found in the backup database
class InsertThread(threading.Thread):
    def __init__(self, data, serverId):
        threading.Thread.__init__(self)
        self.data = data #array of json for specific server id
        self.serverId = serverId

    def run(self):
        #check first if the database available or not
        if self.checkIfConnected():
            self.execute()
        else:
            print("no connection to slave id : " + self.serverId)

    def checkIfConnected(self):
        data = {"server_id": self.serverId}
        try:
            r = requests.post(url=Links.checkConnection, data=data,timeout=(1, 1))
            result = r.json()

            if result["server_response"] == True:
                return True

        except:
            return False
        return False

    def execute(self):
        #database available then send the requests
        size = len(self.data)
        for i in range(size):
            obj = data[i]
            data = {"server_id": obj["server_id"],
                    "user_name": obj["user_name"],
                    "email": obj["email"],
                    "password": obj["password"]}
            print("server_id " + obj["server_id"] + "trying")

            t1 = threading.Thread(target=self.send, args=[data])
            t1.start()

    #send the data to its specific database server
    def send(self, data):
        # it 'll send an insert and delete if success from backup database
        r = requests.post(url=Links.insertBackupToSlave, data=data,timeout=(2, 2))
        result = r.json()


