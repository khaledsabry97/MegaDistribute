import threading
import time

from DatabaseBackupServer.BackupThread import BackupThread


thread1 = BackupThread() #call the backup thread to work
thread1.start()

