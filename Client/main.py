from Data.data import Data
from Functions.Upload import Upload
from IO import IO


global data
data = Data()
def Enter_user(start):

    while (1):
        x = int(input("Hello : " + "\n" + "1) To sign in press 1 \n" + "2) To sign up press 2 "))
        if x == 1:
            #start.signin()
            data.userId = 8
            break
        elif x == 2:
            start.signup()
            break
def usr_action(start):
    while (1):
        x =int(input("1) to upload  press 1 " + "\n"+"2) to download press 2 \n " +"3)to log out press 3 "))
        if x == 1:
             data.currentFilePath = start.getFilePath()
             data.fileName = input("what is the name of your file : ")
             upload = Upload()
             upload.sendUploadReq()
             break
        elif x == 2:
            download()
            break
        elif x==3:
            break


start= IO()

while(1)   :
    Enter_user(start)
    usr_action(start)


