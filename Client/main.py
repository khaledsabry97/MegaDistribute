from tkinter import filedialog

from Connections.ReceiverController import ReceiverController
from Data.data import Data
from Functions.Upload import Upload
from IO import IO
import tkinter as tk


def getFilePath():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path


def Enter_user(start):

    while (1):
        x = int(input("Hello : " + "\n" + "1) To sign in press 1 \n" + "2) To sign up press 2 "))
        if x == 1:
            #start.signin()
            Data.userId = 8
            break
        elif x == 2:
            start.signup()
            break
def usr_action(start):
    while (1):
        #x =int(input("1) to upload  press 1 " + "\n"+"2) to download press 2 \n " +"3)to log out press 3 "))
        x = 1
        if x == 1:
            #'E:/Projects/DS_CFD/Client/adele.mp4'
             #data.currentFilePath = getFilePath()
             Data.currentFilePath =  'E:/Projects/DS_CFD/Client/adele.mp4'
             Data.fileName = input("what is the name of your file : ")
             upload = Upload()
             upload.sendUploadReq()
             break
        elif x == 2:
            #download()
            break
        elif x==3:
            break


start= IO()

Enter_user(start)
usr_action(start)

receiverThread = ReceiverController(3000)
receiverThread.start()


