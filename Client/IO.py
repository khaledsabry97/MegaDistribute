import requests
import tkinter as tk
from tkinter import filedialog

from Connections.DataBaseController import DatabaseController
from Data.data import Data
from Functions.Download import Download
from Functions.Show import Show


class IO:


    @staticmethod
    def getFilePath():
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        return file_path

    @staticmethod
    def check_email_contains(email_address, characters, min_length=6):
        while True:
            for character in characters:
                if character not in email_address:
                    email_address = input(
                        "Your email address must have '{}' in it\nPlease write your email address again: ".format(
                            character))
                    continue
            if len(email_address) <= min_length:
                email_address = input("Your email address is too short\nPlease write your email address again: ")
                continue
            return email_address

    @staticmethod
    def signIn():
        b = True
        while (b):
            username = input("Enter  a username: ")
            password = input("Enter a password: ")
            if len(username) == 0 or len(password) == 0:
                b = True
            else:
                b = False

        result = DatabaseController.signIn(username, password)
        if result == -2:
            print("we are deeply sorry all the database servers are down, please try later!")
            IO.welcome()
        if result == -1:
            print("Check your username/password")
            IO.welcome()
        else:
            print("Logged in Successfully")
            Data.userId = int(result)
            IO.functions()


    @staticmethod
    def signUp():
        b = True
        while (b):
            username = input("Enter  a username: ")
            password = input("Enter a password: ")
            #emailAddress = IO.check_email_contains(input("What is your email address? "), "@.")
            emailAddress = input("Enter an email: ")

            if len(username) == 0 or len(password) == 0 or len(emailAddress) == 0:
                b = True
            else:
                b = False


        result = DatabaseController.signUp(username,password,emailAddress)
        if result == True:
            print("Signed Up Successfully")
        else:
            print("something went wrong !")
        IO.welcome()


    @staticmethod
    def upload():
        #Data.currentFilePath = IO.getFilePath()
        Data.currentFilePath = 'fast.mov'
        Data.fileName = input("what is the name of your file : ")
        from Functions.Upload import Upload
        upload = Upload()
        upload.sendUploadReq()

    @staticmethod
    def download():
        # show filenames

        show = Show ()
        show.snd_shw_req ()
    pass

    @staticmethod
    def welcome():
        print("Welcome, in our app")
        print("[1] Sign Up")
        print("[2] Sign In")
        userAction = int(input())
        if userAction == 1:
            IO.signUp()
        elif userAction == 2:
            IO.signIn()
        else:
            IO.welcome()



    @staticmethod
    def functions():
        print("What do you want to do ?")
        print("[1] Upload")
        print("[2] Download")
        print("[3] LogOut")

        userAction = int(input())
        if userAction == 1:
            IO.upload()
        elif userAction == 2:
            IO.download()

        elif userAction == 3:
            Data.userId = -1
            IO.welcome()

        else:
            IO.welcome()