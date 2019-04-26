import requests

from Data.Links import Links


class DatabaseController:
    ################################
    #Essential Methods#

    #for all inserts, deletes and update queries
    @staticmethod
    def inUpDL(link,data={}):
        r = requests.post(url=link, data=data, timeout=(1, 2))
        result = r.json()

        try:
            if (result["server_response"] == True):
                return True
        except:
            pass
        return False

    #for all select queries
    def select(links,data={}):
        array = []
        for i in range(len(links)):
            try:
                r = requests.post(url=links[i], data=data,timeout=(0.2, 1))
                result = r.json()
                array = []
                if (result["server_response"] == "server down"):
                    continue
                elif result["server_response"] == False:
                    return array,True
                else:
                    array = result["server_response"]
                    return array,True
            except :
                pass
        return array,False
    #Essential Methods#
    ################################


    @staticmethod
    def signIn(username,password):
        data = {"user_name": username,
                "password": password}
        array, state = DatabaseController.select(Links.signIn(), data)
        if state == False:
            return -2 #no database server connecting
        elif len(array) == 0:
            #not found
            return -1
        return array[0]["id"]

    @staticmethod
    def signUp(username,password,email):
        data = {"user_name": username,
                "password": password,
                "email":email}
        return DatabaseController.inUpDL(Links.signUp, data)
