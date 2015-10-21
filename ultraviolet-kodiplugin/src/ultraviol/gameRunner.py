__author__ = 'developer'

import ultraviol.PlatformProviderSpectrum

import os
import ultraviol.apputils
import shutil
import ultraviol.dataStructures



class gameRunner:


    configuration=None



    def createFolderStructure(self):
        foldername= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME
        if (not os.path.exists(foldername)):
            os.mkdir(foldername)

        confFolder= ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.CONF_FOLDER
        print ("Creating folder :"+confFolder)
        if (not os.path.exists(confFolder)):
            os.mkdir(confFolder)
        print ("Creating db structure")
        if (not os.path.exists(ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.DB_FOLDER)):
            os.mkdir(ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.DB_FOLDER)
            shutil.copy(self.DB_NAME, ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.DB_FOLDER)



    def configureEmulator (self):

        print("Select Zx Spectrum configuration...")

        conf=None
        if (os.path.exists(ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE)):
            print ("if")
            # import json
            # from pprint import pprint
            # with open(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+self.CONF_FOLDER+'configuration.json') as data_file:
            #     conf = json.load(data_file)
            # pprint(conf)

            print("laoding pickle...")
            import pickle
            with open(ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE, 'rb') as f:
                conf= pickle.load(f)

        else:
            conf =ultraviol.dataStructures.configuration()
            fuseCommand = input ("Configure your fuse program name:")
            conf.fuseCommand= fuseCommand

            print("Select model.")
            # print (os.path("."))
            print(os.path.dirname(os.path.realpath(".")))
            models =os.listdir(self.BIOSFOLDER)
            i=0
            for model in models:
                print("(%d) model %s..." % (i, model))
                i +=1

            modelOpt = ultraviol.apputils.getInput("Select model:",i)

            selectedModel = models[int(modelOpt)]

            print("Select available bios-es for the model %s " % selectedModel)

            bioses =os.listdir(self.BIOSFOLDER+selectedModel)
            i=0
            for bios in bioses:
                print("(%d) bios %s..." % (i, bios))
                i +=1

            biosOpt = ultraviol.apputils.getInput("Select bios:",i)

            selectedBios = bioses[int(biosOpt)]


            conf.model= selectedModel
            conf.bios= selectedBios

            # jsonConf= JSONEncoder.encode(conf)
            # import json
            # with open(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.CONF_FOLDER+ultraviolet.gameRunner.gameRunner. CONF_FILE, 'w+') as outfile:
                # json.dump(jsonConf, outfile)
                # json.dumps(conf, default=lambda o: o.__dict__,
                #               sort_keys=True, indent=4)
            # with open(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.gameRunner.gameRunner.CONF_FOLDER+ultraviolet.gameRunner.gameRunner. CONF_FILE, "w+") as outfile:
            #     # json.dump(conf, outfile, indent=2)
            #     json.dump(conf, cls=CustomEncoder)

            downloadOptList=[]
            downloadOptList.append("True")
            downloadOptList.append("False")

            print("(0) True")
            print("(1) False")

            downloadOpt = ultraviol.apputils.getInput("Keeo downloaded games", 2)
            print("opt: %s" % downloadOpt)
            download = downloadOptList[int(downloadOpt)]
            conf.download= bool(download)

            print("Writing pickle...")
            import pickle
            with open(ultraviol.apputils.getConfFolder()+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE, 'bw+') as f:
                pickle.dump(conf, f)

        print("Model: %s bios: %s " % (conf.model, conf.bios))
        return conf


    def runGame (self):

        self.createFolderStructure()
        conf = self.configureEmulator()
        ultraviol.gameRunner.gameRunner.configuration= conf
        #provider = platform.PlatformProviderSpectrum()
        provider = ultraviol.PlatformProviderSpectrum.PlatformProviderSpectrum()

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

        provider.playRom(ultraviol.apputils.cleanStringOs(selectedModel) ,ultraviol.apputils.cleanStringOs(selectedBios) ,ultraviol.apputils.cleanStringOs(fullRomName))

        # artFile = provider.downloadArt(selectedGame)
        #
        # coverFile = provider.downloadCover(selectedGame)
        #
        # summaryFile = provider.downloadSummary(selectedGame)


        # provider.closeRom(selectedGame)

        shutil.rmtree("tmp.file")
