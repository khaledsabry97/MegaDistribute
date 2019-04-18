from Connections.ReceiverController import ReceiverController
from Functions.PublisherLive import PublisherLive
from listener import por
from read import Read


receiverThread = ReceiverController()
thread = PublisherLive()
thread2 = Read()
thread3 = por()

receiverThread.start()
thread.start()
thread2.start()
thread3.start()