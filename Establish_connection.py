import socket



class connection :

    def Get_IP(self):
        hostname = socket.gethostname()
        return (socket.gethostbyname(hostname))


