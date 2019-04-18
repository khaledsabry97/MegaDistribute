from PublisherLive import PublisherLive
from listener import por
from read import Read
thread = PublisherLive()
thread2 = Read()
thread3 = por()
thread.start()
thread2.start()
thread3.start()