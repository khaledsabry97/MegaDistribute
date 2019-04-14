import requests

from Data.Links import Links


class DatabaseController:

    @staticmethod
    def getLessThan3Duplication():
        r = requests.post(url=Links.getLessThan3Duplication, data={})
        result = r.json()

        if (result["server_response"] != "server down" and result["server_response"] != False):
            array = result["server_response"]
            return array
        return []


    @staticmethod
    def addDuplicateNoSuccess(userId,nodeId,fileName):
       pass

    @staticmethod
    def deleteDuplicateMoreThanOneDayNoSuccess():
        pass