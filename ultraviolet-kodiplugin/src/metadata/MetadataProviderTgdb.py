__author__ = 'developer'

class MetadataProviderTgdb:
    id=1
    name ="The Games DB"
    url = "http://thegamesdb.net/"

def __init__ (self):
    print ("initiating metadata provider"+self.name)


    def getArt (self, name):
        return "art"

    def getCover(self, name):
        return "cover"

    def getSummary(self, name):
        return "summary"
