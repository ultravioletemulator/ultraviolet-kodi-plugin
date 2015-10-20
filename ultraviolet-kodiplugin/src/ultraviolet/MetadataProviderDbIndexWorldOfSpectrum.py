__author__ = 'developer'

import urllib3
import shutil
import xml.dom.minidom
import ultraviolet.dataStructures
import requests
from lxml import html
import ultraviolet.gameRunner

import os

class MetadataProviderDbIndexWorldOfSpectrum:
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

        gameId=-1
        import sys
        import os
        import sqlite3 as lite
        resGameList = []

        try:
            dbName= os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.DB_NAME
            print("Dbname %s " % dbName)

            con = lite.connect(dbName)

            cur = con.cursor()
            # cur.execute('SELECT SQLITE_VERSION()')
            print("saving game: %s " % (game))
            sql = 'Select * from  GAMES WHERE NAME like "%'+game+'%"'
            cur.execute(sql)

            for tuple in cur.fetchall():
                r = ultraviolet.dataStructures.reg(cur, tuple)
                game= ultraviolet.dataStructures.Game()
                game.name = r.name
                game.id = r.id
                resGameList.append(game)

                # data = cur.fetchone()
                # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.commit()
                con.close()

        return resGameList




    def queryGameList(self, gameName):

        con = None
        import sys
        import os
        import sqlite3 as lite
        try:
            con = lite.connect(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.DB_NAME)

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


    def getRom (self, game):
        print ("Getting rom:"+game.id)

        import sys
        import os
        import sqlite3 as lite
        resGameList = []

        try:
            con = lite.connect(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.DB_NAME)

            cur = con.cursor()
            # cur.execute('SELECT SQLITE_VERSION()')
            print("getting game: (%s) %s " % (game.id, game.name))
            sql = 'Select * from  GAMES WHERE ID = "'+game.id+'"'
            cur.execute(sql)

            for tuple in cur.fetchall():
                r = ultraviolet.dataStructures.reg(cur, tuple)
                game = ultraviolet.dataStructures.Game()
                game.name = r.name
                game.id = r.id

                resGameList.append(game)

                # data = cur.fetchone()
                # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.commit()
                con.close()
        return resGameList


    def getGameFiles (self, game):
        print ("Getting rom: %d " % game.id)

        gameId=-1
        import sys
        import os
        import sqlite3 as lite
        resFileList = []

        try:
            con = lite.connect(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.DB_NAME)

            cur = con.cursor()
            # cur.execute('SELECT SQLITE_VERSION()')
            print("getting game: (%s) %s " % (game.id, game.name))
            sql = 'Select * from  GAMEFILES WHERE GAMEID = "'+str(game.id)+'"'
            cur.execute(sql)

            for tuple in cur.fetchall():
                r = ultraviolet.dataStructures.reg(cur, tuple)
                file = ultraviolet.dataStructures.File()
                file.name = r.name
                file.id = r.id
                file.gameId = r.gameId
                file.url = r.url
                resFileList.append(file)
                # game.files.append(file)

                # data = cur.fetchone()
                # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.commit()
                con.close()
        return resFileList



    def getGameById (self, platform, gameId):
        print("Searching for platform %s and game %s " % (platform, gameId))

        #gameId=-1
        import sys
        import os
        import sqlite3 as lite

        game = ultraviolet.dataStructures.Game()
        try:
            con = lite.connect(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.DB_NAME)

            cur = con.cursor()
            # cur.execute('SELECT SQLITE_VERSION()')
            print("saving game:  %s" % ( gameId))
            sql = 'Select id, name, url from  GAMES WHERE ID ='+str(gameId)
            cur.execute(sql)

            res = cur.fetchone()
            if (not res== None):
                # for tuple in res:
                    #r = ultraviolet.dataStructures.reg(cur, tuple)
                    game.name = res[1]
                    game.id = res[0]
                    game
                    # data = cur.fetchone()
                    # print ("SQLite version: %s" % data)
        except lite.Error as e :
            print("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.commit()
                con.close()

        return game


    def downloadRom (self, file):
        print("Downloading game %s from url %s ..." % (file.name, file.url))
        tmpFileName = ultraviolet.apputils.downloadFile (file.url, file.name,)
        print ("Done saving")
        return file
        # print ("Unzipping file %s " % tmpFileName)

        # fileName= os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_FOLDER+file.name
        # ultraviolet.apputils.unzipFile (fileName, tmpFileName)



    def getArt (self, name):
        return "art"

    def getCover(self, name):

        return "cover"

    def getSummary(self, name):
        return "summary"


