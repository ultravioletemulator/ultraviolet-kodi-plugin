__author__ = 'developer'

import urllib3
import shutil
import xml.dom.minidom
import dataStructures


class MetadataProviderTgdb:
    id=1
    name ="The Games DB"
    url = "http://thegamesdb.net/"

    SPECTRUM_ID = 4913  # ZX Spectrum id
    SPECTRUM_NAME="Sinclair+ZX+Spectrum"
    urlList = "http://thegamesdb.net/api/GetGamesList.php?platform="+SPECTRUM_NAME+"&name="
    urlGame = "http://thegamesdb.net/api/GetGame.php?id="
    urlArt = "http://thegamesdb.net/api/GetArt.php?id="
    urlPlatform = "http://wiki.thegamesdb.net/index.php/GetPlatform.php?id="
    urlPlatformList = "http://wiki.thegamesdb.net/index.php/GetPlatformsList.php"


# http://www.worldofspectrum.org/games/b.html
    #id WOS

    def searchGame (self, platform, game):
        print("Searching for platform %s and game %s " % (platform, game))
        # usock = urllib3.urlopen(self.urlList+game)

        url = self.urlList+game
        # print(url)
        http = urllib3.PoolManager()
        usock = http.urlopen('GET',url, preload_content=False)

        # xmldoc = xml.dom.minidom.parse(usock)
        # print (xmldoc.toxml())

        import xml.etree.ElementTree
        e = xml.etree.ElementTree.parse(usock).getroot()
        games = e.findall("Game")
        res = []

        for g in games:
            searchResult = dataStructures.searchResult()
            searchResult.id=g.find("id").text
            # print(searchResult.id)
            searchResult.name=g.find("GameTitle").text
            # print(searchResult.name)
            res.append(searchResult)
        return res



    def getArt (self, name):
        return "art"

    def getCover(self, name):
        return "cover"

    def getSummary(self, name):
        return "summary"


