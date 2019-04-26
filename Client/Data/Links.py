from Data.data import Data


class Links:
    ip = Data.getDatabaseSlaveIp()
    signUp = "http://" + Data.getDatabaseMaster() + "/DS/create_user.php"


    @staticmethod
    def signIn():
        data = Data.getDatabaseSlaveIp()
        arr = []
        for i in range(len(data)):
            arr.append("http://"+data[i]+"/DS/Slave/sign_in.php")

        arr.append("http://" + Data.getDatabaseMaster() + "/DS/sign_in.php")
        return arr