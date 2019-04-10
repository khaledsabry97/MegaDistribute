import threading
import requests

from DatabaseBackupServer.links import Links


class InsertThread(threading.Thread):
    def __init__(self, data, serverId):
        threading.Thread.__init__(self)
        self.data = data
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
            r = requests.post(url=Links.checkConnection, data=data)
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
            thread = InsertThread(Links.insertBackupToSlave, data)
            thread.start()
            t1 = threading.Thread(target=self.send, args=[data])
            t1.start()

    def send(self, data):
        r = requests.post(url=Links.insertBackupToSlave, data=self.data)
        result = r.text
