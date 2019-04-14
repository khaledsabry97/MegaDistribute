
from Data.Datakeepers import DataKeepers
from Functions.Duplicate import Duplicate
from Functions.SubscriberLive import SubscriberLive

DataKeepers.inialize()


thread = SubscriberLive()
thread2 = Duplicate()
thread.start()
thread2.start()
