


class PlatformProvider(Interface):



    def getName (self):
        return None

    def searchRom (query):
        return ['1','2','3']

    def downloadRom (name):
        return "Zip file"

    def listFile (file):
        return ['rom1','rom2']

    def playRom (name):
        return 1


    def downloadArt (name):
        return "art"

    def downloadCover(name):
        return "cover"

    def downloadSummary(self,name):
        return "summary"



