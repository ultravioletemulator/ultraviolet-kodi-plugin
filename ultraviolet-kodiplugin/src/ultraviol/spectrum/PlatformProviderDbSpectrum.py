import ultraviol.dataStructures
import shutil
import os

import ultraviol.spectrum.MetadataProviderDbIndexWorldOfSpectrum as mpWos

class PlatformProviderSpectrum:
    id = 1
    name = "Zx Spectrum"
    conf=None
    metadataProvider = mpWos.MetadataProviderDbIndexWorldOfSpectrum()


    def f(self):
        return 'hello world'


    def searchRom (self, queryString):

        # metadataProvider = MetadataProviderTgdb.MetadataProviderTgdb()
        #metadataProvider = ultraviolet.MetadataProviderWorldOfSpectrum.MetadataProviderWorldOfSpectrum()

        games = self.metadataProvider.searchGame(mpWos.MetadataProviderDbIndexWorldOfSpectrum.SPECTRUM_ID, queryString)
        resGameList = []
        resGameIdList = []
        i=0
        for game in games:
            gameId = game.id
            gameTitle = game.name
            print("(%s) %s (%d)" % (i, gameTitle, gameId))
            resGame = ultraviol.dataStructures.Game()
            resGame.name = gameTitle
            resGame.id = gameId
            resGame.url = game.fileUrl
            resGame.fileUrl= game.fileUrl
            resGameIdList.append(resGame.id)
            resGameList.append(resGame)
            i +=1

        selectedGameIdx = ultraviol.apputils.getInput ("Please enter the id of the game you want to play.",i)
        selectedGame = resGameList[int(selectedGameIdx)]
        selectedGameId= resGameIdList[int(selectedGameIdx)]
        print ("Selected game: %d " % selectedGameId)
        game = self.metadataProvider.getGameById(self.name, selectedGameId)
        print ("Game: %d " % selectedGameId)
        print(game)
        return game




        # def sRom (query):
    #     print(" searching for rom: %s" % (query))
    #     return ['1', '2', '3']

    def getRom(self, game):
        print ("getRom...")
        print(game)

        files = self.metadataProvider.getGameFiles(game)
        i = 0
        for file in files:
            print("(%d) %s " % (i, file.name))
            i +=1
        selectedFileIndex = ultraviol.apputils.getInput("Select file", i)

        selectedFile = files[int(selectedFileIndex)]

        game.fileUrl= selectedFile.url
        game.files.append(selectedFile)

        file = self.metadataProvider.downloadRom(selectedFile)
        return file
        # ultraviolet.apputils.unzipFile()



    def listFile (self, name):
        return ['rom1','rom2']


    def playRom (self, model, bios, name, conf):
        print("Playing rom: %s" % name)
        print("Model %s bios %s" % (model, bios))

        try:
            shutil.rmtree(ultraviol.configuration.TMP_FOLDER+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER)
        except:
            print("")

        if (bios.endswith(".zip")):
            nameClean=bios.replace(".zip", "")
            ultraviol.apputils.unzipFile(ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER, ultraviol.configuration.BIOSFOLDER +model+"/"+bios)

        # os.system("fuse-sdl "+name+" --rom-128 bios/"+bios)
        bioses = os.listdir(ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER)
        biosStr=""
        for bios in bioses:
            biosStr += ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+bios+" "

        # command = "fuse-sdl "+name+" --rom-speccyboot "+biosStr
        #command = "fuse-sdl "+name+" --speed 100 --full-screen --graphics-filter hq3x  -j  --rom-"+model+" "+biosStr
        biosCommand= self.getBiosCommand(model, bios)
        command = ultraviol.gameRunner.gameRunner.configuration.fuseCommand+" "+name+ biosCommand+" --fastload  --speed 100 --full-screen --graphics-filter hq3x  -j "+conf.inputPath+" --joystick-1-output 3 "
        print(command)
        os.system(command)
        return 1

    def getBiosCommand (self, model, bios):
        biosName= bios.replace(".zip","")
        biosName= biosName.replace(".rom","")
        biosName= biosName.replace("-0","")
        biosName= biosName.replace("-1","")
        res=""
        if model =="48":
            res= " --machine "+model+" --rom-"+model+" "+bios
        elif model =="128":
            res = " --machine "+model+" --rom-"+model+"-0 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-1.rom "
        elif model=="plus2":
            res = " --machine "+model+" --rom-"+model+"-0 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-1.rom "
        elif model=="plus3":
            res = " --machine "+model+" --rom-"+model+"-0 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-1.rom  --rom-"+model+"-2 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-2.rom --rom-"+model+"-3 "+ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER+biosName+"-3.rom "
        return res

    def downloadArt (self, name):
        return "art"


    def downloadCover (self, name):
        return "cover"


    def downloadSummary (self, gameName):
        print("Downloading summary for %s..." % (gameName))
        return "summary"

    def closeRom (self, game):
        print("Closing  %s" % game.name)
        shutil.rmtree("./"+game.name)

    def listZipRoms (self, game):
        from os import listdir
        files = listdir(ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+game.name)
        return files


