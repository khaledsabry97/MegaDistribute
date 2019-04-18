
import requests
import tkinter as tk
from tkinter import filedialog

class IO :

    def Get_file_path(self):
      root = tk.Tk()
      root.withdraw()

      file_path = filedialog.askopenfilename()
      return file_path

    def check_email_contains(email_address, characters, min_length=6):
        while True:
            for character in characters:
                if character not in email_address:
                    email_address = input("Your email address must have '{}' in it\nPlease write your email address again: ".format(character))
                    continue
            if len(email_address) <= min_length:
                email_address = input("Your email address is too short\nPlease write your email address again: ")
                continue
            return email_address

    def signin(self):
        while (1):
            name = input("Enter  username: ")
            password = input("Enter password: ")

            # contain ip of the master
            URL = ""

            PARAMS = {'name': name,
                      'pass': password,
                      'func': 'sign_in'
                      }

            # sending get request and saving the response as response object
            r = requests.post(url=URL, data=PARAMS)

            # extracting data in json format
            data = r.json()

            if data['success'] == 1:
                break
            else:
                print("wrong username or password ")

    def signup(self) :
        while (1):
            name = input("Enter  a username: ")
            password = input("Enter a password: ")
            email_address = self.check_email_contains(input("What is your email address? "), "@.")

            # contain ip of the master
            URL = ""

            PARAMS = {'name': name,
                      'pass': password,
                      'email':email_address,
                      'func': 'sign_up'
                      }

            # sending get request and saving the response as response object
            r = requests.post(url=URL, data=PARAMS)

            # extracting data in json format
            data = r.json()

            if data['success'] == 1:
                break
            else:
                print("server down ")