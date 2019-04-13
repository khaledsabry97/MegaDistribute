import random
import time


class DataKeepers:
    instance = None

    global dks
    dks = {}
    global ports
    ports = {}

    @staticmethod
    def getInstance(self):
        if DataKeepers.instance == None:
            DataKeepers()

        return DataKeepers.instance

    def __init__(self):
        if DataKeepers.instance == None:
            DataKeepers.instance = self
            self.inialize()

    def inialize(self):
        dks[1] = [0,"192.168.0.0" ]
        ports[1] = [7000, 7002, 7004]
        dks[2] = [0, "192.168.0.0" ]
        ports[2] = [8000, 8002, 8004]
        dks[3] = [0,"192.168.0.0"  ]
        ports[3] = [9000, 9002, 9004]

    #update time for selected port id
    def updateTime(self,id):
        if id in dks:
            print("Data Node "+id+" : "+dks[id][0]+" to "+dks[id][0])
            dks[id][0] = int(time.time() * 1000)
        else:
            print("didn't fint that id")

    #get random port for selected node id
    def getRandomPort(self,id):
        if id in ports:
            print("Data Node "+id+" : "+dks[id][0]+" to "+dks[id][0])
            portid = random.randint(len(ports[id]))
            return ports[id][portid]
        else:
            print("didn't fint that id")
            return -1

    #get random alive data nodes
    #you can pass the ids of nodes that you don't want to see in the result by defualt empty
    def getAliveDataNodesExclude(self,id=[]):
        # assign it if you put one or two nodes that you don't want to see them
        node1 = -1
        node2 = -1
        if len(id) == 1:
            node1 = id[0]
        elif len(id) == 2:
            node2 = id[1]

        arr = [] #array to insert all the potential selected ids for the node
        for i in range(1, len(list(dks.keys())) + 1):
            if self.checkIfAlive(i) and i != node1 and i != node2:
                arr.append(i)
        if len(arr) > 0:
            random.shuffle(arr) #randomize the array of nodes
            return arr
        else:
            print("no nodes found")
            return -1

    #pass node id and see if it's alive or not
    def checkIfAlive(self,id):
        if int(time.time() * 1000) - dks[id][0] <= 1000:
            return True
        return False

    #get ports to send it to user
    #you must path the nodes ids that you want to get the ports for it
    #you should path the size you want by defult = 6
    #first output 'll be an array of ports
    #sec. output 'll be true if the size you sent back to you if less than the size you sent then it 'll return false
    #third output 'll be the size of the comming array of ports
    def getPorts(self,nodeIds,size = 6):
        arr = []
        for i in range(len(nodeIds)):
            if self.checkIfAlive(nodeIds[i]):
                for j in range(len(ports[nodeIds[i]])):
                    arr.append(ports[nodeIds[i]][j])

        random.shuffle(arr)
        if len(arr) >= size:
            return arr[0,size],True,size
        else:
            return arr,False,len(arr)


    #return DataNodeIp for node id
    def getDataNodeIp(self,nodeId):
        if nodeId in self.dks:
            return dks[nodeId][1]
        else:
            return  "-1" # not found









