from Connections.ReceiverController import ReceiverController
from Functions.PublisherLive import PublisherLive


receiverThread1 = ReceiverController(6000)
receiverThread2 = ReceiverController(6002)
receiverThread3 = ReceiverController(6004)
publisherThread = PublisherLive()

receiverThread1.start()
receiverThread2.start()
receiverThread3.start()
publisherThread.start()