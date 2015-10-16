__author__ = 'developer'

import urllib3
import shutil
import xml.dom.minidom
import dataStructures


class MetadataProviderWorldOfSpectrum:
    id=1
    name ="The Games DB"
    url = "http://thegamesdb.net/"

    SPECTRUM_ID = 4913  # ZX Spectrum id
    SPECTRUM_NAME="Sinclair+ZX+Spectrum"
    urlHost="http://www.worldofspectrum.org/"
    urlList = "http://www.worldofspectrum.org/games/"  #b.html
    urlGame = "http://thegamesdb.net/api/GetGame.php?id="
    urlArt = "http://thegamesdb.net/api/GetArt.php?id="
    urlPlatform = "http://wiki.thegamesdb.net/index.php/GetPlatform.php?id="
    urlPlatformList = "http://wiki.thegamesdb.net/index.php/GetPlatformsList.php"



# http://www.worldofspectrum.org/games/b.html
    #id WOS

    def searchGame (self, platform, game):
        print("Searching for platform %s and game %s " % (platform, game))
        # usock = urllib3.urlopen(self.urlList+game)

        url = self.urlList+(game[0]).lower()+".html"
        # print(url)
        # http = urllib3.PoolManager()
        # usock = http.urlopen('GET',url, preload_content=False)

        from lxml import html
        import requests
        print ("Getting letter index...")
        page = requests.get(url)
        print(page.text)
        tree = html.fromstring(page.text)
        # urlGame = tree.xpath('//a[contains(text,"'+game.name+'")]/@href')
        # urlGame = tree.xpath('//A[contains(text,"'+game.name+'")]/@href')
        # xpath ='//a[contains(lower-case(text),lower-case("'+game+'"))]'
        xpath ='//a'
        print(xpath)

        links= tree.xpath(xpath)
        gameList = []
        i=0
        for link in links:
            # print(link)
            href =link.attrib['href']
            # print(href)
            # print ("infoseekid" in href)
            if ("infoseekid" in href):
                gameDesc = link.attrib['href']
                gameTitle = link.text_content()
                gameList.append(gameDesc)
                print("(%d) %s" % (i, gameTitle))
                i += 1
            # print(link.text_content())


        linkSelected = input("Select game")
        print("length: %d index: %d" % (len(gameList), i ))

        gameDescUrl = gameList[int(linkSelected)]

        print("gameDescUrl %s" % gameDescUrl)
        print("Getting description page...")
        pageDownload = requests.get(self.urlHost+gameDescUrl)
        treeDownload = html.fromstring(pageDownload.text)

        gameUrls=[]
        gameTitles=[]
        files = treeDownload.xpath('//a')
        i=0
        for f in files :
            # print(f)
            gameDesc = f.attrib['href']
            # print(gameDesc)
            gameTitle = f.text_content()
            if (".zip" in gameDesc):
                print ("(%d) %s" % (i, gameTitle))
                gameUrls.append(self.urlHost+gameDesc)
                gameTitles.append(gameTitle)
                i +=1

        zipSelected = input("Select game file")
        urlGameZip = gameUrls[int(zipSelected)]


        result = dataStructures.Game()
        result.name = gameTitles[int(zipSelected)]
        result.id = ""
        result.url = urlGameZip
        result.fileUrl = urlGameZip
        print ("You have selected %s %s file: %s" % (result.name, result.url, result.fileUrl))
        resGameList = []
        resGameList.append(result)
        return resGameList



    def getArt (self, name):
        return "art"

    def getCover(self, name):
        return "cover"

    def getSummary(self, name):
        return "summary"


