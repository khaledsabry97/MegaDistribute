import requests as requests
import zmq

from IO.IO import IO


def upload(file_path):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://" + "localhost:5556")
    data = {
        "func": "up"
    }
    print(data["func"])
    socket.send_json(data)
    #  Get the reply.
    data = socket.recv_json()
    ip = data["ip"]
    port = data["port_number"]
    socket.connect("tcp://" + ip + ":" + port)
    f = open(file_path, "rb")
def download():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://" + "localhost:5556")
    data = {
        "func": "down"
    }
    print(data["func"])
    # socket.send_json(data)
    # Get the reply.

    # data = socket.recv_json()
    # get ip and ports
    f = open("video.mp4", "rb")
    video = f.read(10)
    data = {
        "video": video,
        "filename": "video.mp4",
        "func": "uploading"
    }
def Enter_user(start):
    while (1):
        x = int(input("Hello : " + "\n" + "1) To sign in press 1 \n" + "2) To sign up press 2 "))
        if x == 1:
            start.signin()
            break
        elif x == 2:
            start.signup()
            break
def usr_action(start):
    while (1):
        x =int(input("1) to upload  press 1 " + "\n"+"2) to download press 2 \n " +"3)to log out press 3 "))
        if x == 1:
             upload(start.Get_file_path())
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


