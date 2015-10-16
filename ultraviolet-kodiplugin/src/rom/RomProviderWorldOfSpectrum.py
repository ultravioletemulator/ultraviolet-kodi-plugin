
class RomProviderWorldOfSpectrum:
    id=1
    name = "World of Spectrum"
    url = "http://www.worldofspectrum.org/archive.html"

    __all__ = ["RomProviderWorldOfSpectrum"]

    def __init__(self):
        print("initiating rom provider"+self.name)


    def searchRom (self,query):
            return ['1','2','3']

    def downloadRom (self,name):
            return "Zip file"

    def indexContent (self)