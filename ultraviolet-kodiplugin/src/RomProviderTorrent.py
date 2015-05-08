import TorrentSearchProvider

class RomProviderWorldOfSpectrum:
    id=1
    name ="World of Spectrum"
    url ="http://www.worldofspectrum.org/"

    TorrentSearchProvider tSearchProvider=  TorrentSearchProvider()


def __init__ (self):
    print ("initiating rom provider"+self.name)



    def searchRom (self, query):
        return tSearchProvider.search (query)


    def downloadRom (name):
        return "Zip file"
