__author__ = 'developer'



import os
import ultraviol.apputils
import shutil
import ultraviol.dataStructures

import ultraviol.spectrum.PlatformProviderDbSpectrum as pps
import ultraviol.configuration

class gameRunner:


    APP_HOME="/ultraviolet/"
    PKG_HOME="/ultraviol/"
    CONF_FOLDER="configuration/"
    CONF_FILE="configuration.pickle"

    configuration=None




    def runGame (self):

        # ultraviol.configuration.createFolderStructure()
        # conf = ultraviol.configuration.configureEmulator()
        conf = ultraviol.configuration.loadConfiguration()
        ultraviol.gameRunner.gameRunner.configuration= conf
        #provider = platform.PlatformProviderSpectrum()
        provider = pps.PlatformProviderSpectrum()

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

        unzipFolderName =  ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+gameFile.name
        print("Unzipping to : %s" % (unzipFolderName))
        if (not os.path.exists(unzipFolderName)):
            os.mkdir(unzipFolderName)

        ultraviol.apputils.unzipFile(ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+gameFile.name,ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_FILE)
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
        fullRomName = ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+gameFile.name+"/"+rom


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



