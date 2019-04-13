import time
from threading import Thread, Lock

from Datakeepers import DataKeepers
from SubscriberLive import SubscriberLive

DataKeepers.inialize()


thread = SubscriberLive()
thread.start()
