__author__ = 'developer'

import urllib3
import shutil
import xml.dom.minidom
import dataStructures
import requests
from lxml import html

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
        # print(page.text)
        tree = html.fromstring(page.text)
        # urlGame = tree.xpath('//a[contains(text,"'+game.name+'")]/@href')
        # urlGame = tree.xpath('//A[contains(text,"'+game.name+'")]/@href')
        # xpath ='//a[contains(lower-case(text),lower-case("'+game+'"))]'
        xpath ='//a'
        # print(xpath)

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
        print ("GameUrl: "+urlGameZip)


        result = dataStructures.Game()
        result.name = gameTitles[int(zipSelected)]
        result.id = ""
        result.url = urlGameZip
        result.fileUrl = urlGameZip
        print ("You have selected %s %s file: %s" % (result.name, result.url, result.fileUrl))
        resGameList = []
        resGameList.append(result)
        return resGameList

    def indexGames (self):
        print("indexing games...")
        index = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","ñ","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        for letter in index:
            self.indexLetter(letter)

    def indexLetter(self, letter):
        print("Searching for platform %s and letter %s " % (MetadataProviderWorldOfSpectrum.SPECTRUM_ID, letter))

        url = self.urlList+(letter).lower()+".html"

        from lxml import html
        import requests
        print ("Getting letter index...")
        page = requests.get(url)
        # print(page.text)
        tree = html.fromstring(page.text)

        xpath ='//a'
        print(xpath)
        links= tree.xpath(xpath)
        gameList = []
        gameTitleList = []
        i=0
        for link in links:
            # print(link)
            href =link.attrib['href']
            # print(href)
            # print ("infoseekid" in href)
            if ("infoseekid" in href):
                gameDesc = link.attrib['href']
                gameTitle = link.text_content()
                gameTitleList.append(gameTitle)
                gameList.append(gameDesc)
                print("(%d) %s" % (i, gameTitle))
                i += 1
                # print(link.text_content())

        i=0
        for game in gameList:
            self.indexGame(gameTitleList[i], game)
            i +=1


    def indexGame (self,  gameTitle, gameUrl):
        print("indexing game: %s" % gameTitle)
        game = dataStructures.Game()
        game.name= gameTitle
        game.gameUrl= gameUrl


        gameDescUrl = gameUrl

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

        # Add Zips
        resGameList = []
        i=0
        for zip in gameTitles:
            result = dataStructures.File()
            result.fileName = gameTitles[i]
            result.url = gameUrls[i]
            print ("Adding %s file: %s" % (result.fileName, result.url))
            resGameList.append(result)
            i +=1

        game.files= resGameList
        print("Indexed %d files for game %s" % (len(resGameList), game.name))
        self.persistGame (game)


    def persistGame(self, game):
        print("Persisting game %s ..." % game.name)


    def getArt (self, name):
        return "art"

    def getCover(self, name):
        return "cover"

    def getSummary(self, name):
        return "summary"


