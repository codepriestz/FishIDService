from pymongo import MongoClient


    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        return  client.facialrecognition



class mongoaccess:
    def __init__(self):
          self.mongo=connect()

    def add(self,collection,data):
            self.mongo[collection].insert_one(data)
    def find(self,collection,data):
            obj= self.mongo[collection].find_one(data)
            return obj

    def findall(self, collection, data):
        obj = self.mongo[collection].find(data)
        return obj
    def addmany(self,collection,data):
            self.mongo[collection].insert_many(data)

