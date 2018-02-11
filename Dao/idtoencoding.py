class idencoding:
    def __init__(self):
            self.mongo=mongoaccess()
    def add(self,data):
            self.mongo.add('idencoding',data)

    def addmany(self, data):
            self.mongo.addmany('idencoding', data)

    def find(self, data):
            return self.mongo.find('idencoding', data)
    def findall(self, data):
            return self.mongo.findall('idencoding', data)