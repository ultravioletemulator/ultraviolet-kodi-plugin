import httplib
import urllib2
import xml.etree.ElementTree as ET
import MetadataInfo

class MetadataProviderTgdb:
    id=1
    name ="The Games DB"
    url ="http://thegamesdb.net/"
    apiUrl="http://thegamesdb.net/api"
#http://thegamesdb.net/api/GetGame.php?id=2

def __init__ (self):
    print ("initiating metadata provider"+self.name)



    def importMetadata (game):
            metaData = MetadataInfo()
            baseImgUrl= game.findall ("./baseImgUrl/text()")
            metaData.baseImgUrl= baseImgUrl
            metaData.name= game.findall ("./GameTitle/text()")
            metaData.id=game.findall("./id/text()")
            metaData.releaseDate=game.findall("./ReleaseDate/text()")
            metaData.genres = game.findall("./Genres/Genre/text()")
            metaData.platform=game.findall("./Platform/text()")
            metaData.overview= game.findall("./Overview/text()")
            metaData.rating= game.findall("./Rating/text()")
            boxart=game.findall("./boxart/text()")
            metaData.boxArtUrl = baseImgUrl+boxart
            response =urllib2.urlopen(metaData.boxArtUrl)
            boxartImg=response.read()
            metaData.boxArtImg=boxartImg
            return metaData



    def searchGame (self, platform, name):
        c = httplib.HTTPConnection (self.apiUrl,80);
        gameListXml= c.request('GET', "/GetGamesList?name="+name+"&platform="+platform)
        root = ET.parse (gameListXml)
        games=root.findall ("/Data/Game")
        resGames= []
        for game in games:
            metadata = self.importMetadata(game)
            resGames.extend(game)
        return resGames;

    def getInfo (self, id):
        c = httplib.HTTPConnection (self.apiUrl,80);
        gameListXml= c.request('GET', "/GetGame?id="+id)
        root = ET.parse (gameListXml)
        games= gameList =root.findall ("/Data/Game")
        resGames= []
        for game in games:
            metaData = self.importMetadata (game)
            resGames.extend(metaData)
        return resGames




    def getPlatformGames (self, platformId):

        #http://thegamesdb.net/platform/sinclair-zx-spectrum/

        c = httplib.HTTPConnection (self.apiUrl,80);
        gameListXml= c.request('GET', "/GetPlatformGames?&platform="+platformId)
        root = ET.parse (gameListXml)
        games=root.findall ("/Data/Game")
        resGames= []
        for game in games:
            metadata = self.importMetadata(game)
            resGames.extend(game)
        return resGames;




    def downloadArt (self,id):
        return None

    def downloadCover(self,id):
        c = httplib.HTTPConnection (self.apiUrl,80);
        gameListXml= c.request('GET', "/GetGame?id="+id)
        root = ET.parse (gameListXml)
        game= root.findall ("/Data/Game")

        baseImgUrl= game.findall ("./baseImgUrl/text()")
        id=game.findall("./id/text()")
        boxart=game.findall("/Data/Game/boxart/text()")
        fullBoxart= baseImgUrl+boxart

        response =urllib2.urlopen(fullBoxart)
        boxartImg=response.read()
        return boxartImg

    def downloadOverview(self,id):
        c = httplib.HTTPConnection (self.apiUrl,80);
        gameListXml= c.request('GET', "/GetGame?id="+id)
        root = ET.parse (gameListXml)
        game=root.findall ("/Data/Game")
        id=game.findall("./id/text()")
        overview= game.findall("./Overview/text()")
        return overview

