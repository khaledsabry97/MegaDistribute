from Connections.ReceiverController import ReceiverController

from IO import IO


receiverThread = ReceiverController(3000)
receiverThread.start()

try:
    IO.welcome()
except:
    IO.welcome()

