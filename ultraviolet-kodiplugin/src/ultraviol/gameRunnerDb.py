__author__ = 'developer'

import ultraviol.PlatformProviderSpectrum

import os
import ultraviol.apputils
import shutil
import ultraviol.dataStructures

import ultraviol.PlatformProviderDbSpectrum
import ultraviol.configuration

class gameRunner:


    APP_HOME="/ultraviolet/"
    PKG_HOME="/ultraviol/"
    CONF_FOLDER="configuration/"
    CONF_FILE="configuration.pickle"

    configuration=None




    def runGame (self):

        ultraviol.configuration.createFolderStructure()
        conf = ultraviol.configuration.configureEmulator()
        ultraviol.gameRunner.gameRunner.configuration= conf
        #provider = platform.PlatformProviderSpectrum()
        provider = ultraviol.PlatformProviderDbSpectrum.PlatformProviderSpectrum()

        # provider = PlatformProviderSpectrum()
        # metadataProvider = ultraviolet.MetadataProviderTgdb.MetadataProviderTgdb()

        print(provider)
        print("***********************")
        print(provider.id)
        print(provider.name)
        print("***********************")

        queryString = input("Enter the game name you want to search for:")
        print("Searching for %s..." % queryString)
        selectedGame= provider.searchRom(queryString)

        # romList = provider.sRom(name)

        summary = provider.downloadSummary(selectedGame)
        print(summary)

        gameFile = provider.getRom(selectedGame)

        unzipFolderName =  os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_FOLDER+gameFile.name
        print("Unzipping to : %s" % (unzipFolderName))
        if (not os.path.exists(unzipFolderName)):
            os.mkdir(unzipFolderName)

        ultraviol.apputils.unzipFile(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_FOLDER+gameFile.name,os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_FILE)
        romList = provider.listZipRoms(gameFile)

        print("****************************")
        print("Game: %s " % selectedGame.name)
        print("****************************")
        i = 0
        for rom in romList:
            print("(%d) file %s..." % (i, rom))
            i +=1

        option = ultraviol.apputils.getInput("Please enter the option of the rom you want to play...",i)
        print(option)
        print("Selected file: %s" % option)
        rom = romList[int(option)]
        print("Running file: %s" % rom)
        fullRomName = os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_FOLDER+gameFile.name+"/"+rom


        selectedModel=conf.model
        selectedBios=conf.bios

        provider.playRom(ultraviol.apputils.cleanStringOs(selectedModel) ,ultraviol.apputils.cleanStringOs(selectedBios) ,ultraviol.apputils.cleanStringOs(fullRomName))

        # artFile = provider.downloadArt(selectedGame)
        #
        # coverFile = provider.downloadCover(selectedGame)
        #
        # summaryFile = provider.downloadSummary(selectedGame)

        # provider.closeRom(selectedGame)

        if (os.path.exists("tmp.file")):
            shutil.rmtree("tmp.file")

        if (os.path.exists("tmp")):
            shutil.rmtree("tmp")



