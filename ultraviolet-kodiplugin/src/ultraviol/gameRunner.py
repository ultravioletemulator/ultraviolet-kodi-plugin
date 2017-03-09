__author__ = 'developer'

import ultraviol.spectrum.PlatformProviderSpectrum as pps

import os
import ultraviol.apputils
import shutil
import ultraviol.dataStructures



class gameRunner:


    configuration=None



    def runGame (self):

        self.createFolderStructure()
        conf = self.configureEmulator()
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


        # gameList = provider.searchRom(name)

        # print("Search results:")
        # # PrintRoms
        # i=0
        # for game in gameList :
        #     print("(%d) %s." % (i, game.name))
        #     i+=1
        #
        # option = input("Please enter the option of the game you want to play...")
        #
        # selectedGame = gameList[int(option)]

        gameFile = provider.getRom(selectedGame)

        romList = provider.listZipRoms(selectedGame)

        print("****************************")
        print("%s roms:" % selectedGame.name)
        print("****************************")
        i=0
        for rom in romList:
            print("(%d) rom %s..." % (i, rom))
            i +=1

        option = ultraviol.apputils.getInput("Please enter the option of the rom you want to play...",i)
        print(option)
        print("Selected rom: %s" % option)
        rom = romList[int(option)]
        print("Runnign rom: %s" % rom)
        fullRomName = ultraviol.configuration.TMP_FOLDER+ultraviol.gameRunner.gameRunner.APP_HOME+"tmp/"+selectedGame.name+"/"+rom



        print("Select Zx Spectrum configuration...")
        # print("Select model.")
        # # print (os.path("."))
        # print(os.path.dirname(os.path.realpath(".")))
        # models =os.listdir(self.BIOSFOLDER)
        # i=0
        # for model in models:
        #     print("(%d) model %s..." % (i, model))
        #     i +=1
        #
        # modelOpt = input("Select model:")
        #
        # selectedModel = models[int(modelOpt)]
        #
        #
        #
        # print("Select available bios-es for the model %s " % selectedModel)
        #
        # bioses =os.listdir(self.BIOSFOLDER+selectedModel)
        # i=0
        # for bios in bioses:
        #     print("(%d) bios %s..." % (i, bios))
        #     i +=1
        #
        # biosOpt = input("Select bios:")
        #
        # selectedBios = bioses[int(biosOpt)]

        selectedModel=conf.model
        selectedBios=conf.bios

        provider.playRom(ultraviol.apputils.cleanStringOs(selectedModel) ,ultraviol.apputils.cleanStringOs(selectedBios) ,ultraviol.apputils.cleanStringOs(fullRomName),conf)

        # artFile = provider.downloadArt(selectedGame)
        #
        # coverFile = provider.downloadCover(selectedGame)
        #
        # summaryFile = provider.downloadSummary(selectedGame)


        # provider.closeRom(selectedGame)

        shutil.rmtree("tmp.file")
