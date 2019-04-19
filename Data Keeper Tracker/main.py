from Connections.ReceiverController import ReceiverController
from Functions.PublisherLive import PublisherLive


receiverThread1 = ReceiverController(7000)
receiverThread2 = ReceiverController(7002)
receiverThread3 = ReceiverController(7004)
publisherThread = PublisherLive()

receiverThread1.start()
receiverThread2.start()
receiverThread3.start()
publisherThread.start()