import time

from Connections.ReceiverController import ReceiverController
from Data.Datakeepers import DataKeepers
from Functions.Duplicate import Duplicate
from Functions.SubscriberLive import SubscriberLive
from Functions.checkNode import checkNode

DataKeepers.inialize()


receiverThread1 = ReceiverController(10000)
receiverThread2 = ReceiverController(10002)
receiverThread3 = ReceiverController(10004)
subscriberLiveThread = SubscriberLive()
duplicateThread = Duplicate()

receiverThread1.start()
receiverThread2.start()
receiverThread3.start()
subscriberLiveThread.start()
duplicateThread.start()

time.sleep(5)


checkNode = checkNode()
checkNode.start()
