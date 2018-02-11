from Dao import mongoaccess


class idname:
    def __init__(self):
            self.mongo=mongoaccess()
    def add(self,data):
            self.mongo.add('idname',data)

    def addmany(self, data):
            self.mongo.addmany('idname', data)

    def find(self, data):
            return self.mongo.find('idname', data)
    def find(self, data):
            return self.mongo.findall('idname', data)


