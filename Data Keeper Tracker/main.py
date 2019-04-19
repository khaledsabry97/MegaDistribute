import sys

from Connections.ReceiverController import ReceiverController
from Data.data import Data
from Functions.PublisherLive import PublisherLive

port1 = int(sys.argv[1])
port2 = port1 + 2
port3 = port1 +4
Data.id = int(sys.argv[2])


receiverThread1 = ReceiverController(port1)
receiverThread2 = ReceiverController(port2)
receiverThread3 = ReceiverController(port3)
publisherThread = PublisherLive()

receiverThread1.start()
receiverThread2.start()
receiverThread3.start()
publisherThread.start()
