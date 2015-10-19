__author__ = 'developer'

import urllib3
import shutil
import xml.dom.minidom
import ultraviolet.dataStructures
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


        result = ultraviolet.dataStructures.Game()
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
        self.createDbStructure()
        self.cleanDb()
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
        game = ultraviolet.dataStructures.Game()
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
            result = ultraviolet.dataStructures.File()
            result.fileName = gameTitles[i]
            result.url = gameUrls[i]
            print ("Adding %s file: %s" % (result.fileName, result.url))
            resGameList.append(result)
            i +=1

        game.files= resGameList
        print("Indexed %d files for game %s" % (len(resGameList), game.name))
        self.persistGame (game)

    def createDbStructure(self):
        print("Creating db structure")

        import sys
        import sqlite3 as lite
        try:
            con = lite.connect('ultraviolet.db')

            cur = con.cursor()
            # cur.execute('SELECT SQLITE_VERSION()')
            print("Creating db...")
            cur.execute("SELECT name FROM sqlite_master WHERE  tbl_name='GAMES';")
            # type='table' AND
            gamesExists = cur.fetchone()
            print("games len: %d ok:%r" % (len(gamesExists) , (not gamesExists == None and len(gamesExists)>0 and not gamesExists[0] == None)))

            if (not gamesExists == None and len(gamesExists)==0): #  and not gamesExists[0] == None
                print("Creating GAMES")
                cur.execute(" CREATE TABLE GAMES ( id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, url VARCHAR )")


            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='GAMEFILES';")
            gameFilesExists =cur.fetchone()
            if (not gameFilesExists == None and len(gameFilesExists)==0): # and not gameFilesExists[0] == None
                print("Creating GAMEFILES")
                cur.execute(" CREATE TABLE GAMEFILES ( id INTEGER PRIMARY KEY  AUTOINCREMENT, gameId Integer, name VARCHAR, url VARCHAR )")

            # data = cur.fetchone()
            # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print ("Error %s:" % e.args[0])
            sys.exit(1)

        finally:

            if con:
                con.commit()
                con.close()

    def cleanDb(self):
        print("Cleaning db...")
        import sys
        import sqlite3 as lite
        try:
            con = lite.connect('ultraviolet.db')
            cur = con.cursor()

            cur.execute("DELETE FROM GAMES ")
            cur.execute("DELETE FROM GAMEFILES ")

            # data = cur.fetchone()
            # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print ("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.commit()
                con.close()



    def persistGame(self, game):

        print("Persisting game %s ..." % game.name)
        gameId=-1
        import sys
        import sqlite3 as lite
        try:
            con = lite.connect('ultraviolet.db')

            cur = con.cursor()
            # cur.execute('SELECT SQLITE_VERSION()')
            print("saving game: %s " % game.name)
            cur.execute("INSERT INTO GAMES ('name') VALUES ('"+ultraviolet.apputils.cleanString (game.name)+"')")
            gameId= cur.lastrowid
            # data = cur.fetchone()
            # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print ("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.commit()
                con.close()

        for file in game.files:
            try:
                con = lite.connect('ultraviolet.db')

                cur = con.cursor()
                # cur.execute('SELECT SQLITE_VERSION()')
                print("saving game: %s %s" % (game.name, gameId))
                sql = "INSERT INTO GAMEFILES ('gameId', 'name','url') VALUES ("+str(gameId)+",'"+ultraviolet.apputils.cleanString (file.fileName)+"','"+file.url+"')"

                cur.execute(sql)
                # data = cur.fetchone()
                # print ("SQLite version: %s" % data)
            except lite.Error as e :
                print ("Error %s:" % e.args[0])
                sys.exit(1)

            finally:
                if con:
                    con.commit()
                    con.close()




    def queryGameList(self, gameName):

        con = None
        import sys
        import sqlite3 as lite
        try:
            con = lite.connect('ultraviolet.db')

            cur = con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')

            data = cur.fetchone()

            print ("SQLite version: %s" % data)

        except lite.Error as e :
            print ("Error %s:" % e.args[0])
            sys.exit(1)

        finally:

            if con:
                con.close()




    def getArt (self, name):
        return "art"

    def getCover(self, name):
        return "cover"

    def getSummary(self, name):
        return "summary"


