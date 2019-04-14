import time
from threading import Thread, Lock

from Datakeepers import DataKeepers
from Duplicate import Duplicate
from SubscriberLive import SubscriberLive

DataKeepers.inialize()


thread = SubscriberLive()
thread2 = Duplicate()
thread.start()
thread2.start()
