import threading
import time

from DatabaseBackupServer.BackupThread import BackupThread



thread1 = BackupThread()
thread1.start()

