import ultraviolet.dataStructures
import urllib3
import shutil
import os

# import MetadataProviderTgdb
import ultraviolet.MetadataProviderDbIndexWorldOfSpectrum

class PlatformProviderSpectrum:
    id = 1
    name = "Zx Spectrum"
    conf=None
    metadataProvider = ultraviolet.MetadataProviderDbIndexWorldOfSpectrum.MetadataProviderDbIndexWorldOfSpectrum()
# def __init__(self):
#     print("initiating platform provider"+self.name)


    def f(self):
        return 'hello world'


    def searchRom (self, queryString):

        # metadataProvider = MetadataProviderTgdb.MetadataProviderTgdb()
        #metadataProvider = ultraviolet.MetadataProviderWorldOfSpectrum.MetadataProviderWorldOfSpectrum()

        games = self.metadataProvider.searchGame(ultraviolet.MetadataProviderDbIndexWorldOfSpectrum.MetadataProviderDbIndexWorldOfSpectrum.SPECTRUM_ID, queryString)
        resGameList = []
        resGameIdList = []
        i=0
        for game in games:
            gameId = game.id
            gameTitle = game.name
            print("(%s) %s (%d)" % (i, gameTitle, gameId))
            resGame = ultraviolet.dataStructures.Game()
            resGame.name = gameTitle
            resGame.id = gameId
            resGame.url = game.fileUrl
            resGame.fileUrl= game.fileUrl
            resGameIdList.append(resGame.id)
            resGameList.append(resGame)
            i +=1

        selectedGameIdx = ultraviolet.apputils.getInput ("Please enter the id of the game you want to play.",i)
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
        selectedFileIndex = ultraviolet.apputils.getInput("Select file", i)

        selectedFile = files[int(selectedFileIndex)]

        game.fileUrl= selectedFile.url

        file = self.metadataProvider.downloadRom(selectedFile)
        return file
        # ultraviolet.apputils.unzipFile()



    def listFile (self, name):
        return ['rom1','rom2']


    def playRom (self, model, bios, name):
        print("Playing rom: %s" % name)
        print("Model %s bios %s" % (model, bios))

        try:
            shutil.rmtree(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER)
        except:
            print("")

        if (bios.endswith(".zip")):
            nameClean=bios.replace(".zip", "")
            ultraviolet.apputils.unzipFile(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER, ultraviolet.gameRunner.gameRunner.BIOSFOLDER +model+"/"+bios)

        # os.system("fuse-sdl "+name+" --rom-128 bios/"+bios)
        bioses = os.listdir(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER)
        biosStr=""
        for bios in bioses:
            biosStr += os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+bios+" "

        # command = "fuse-sdl "+name+" --rom-speccyboot "+biosStr
        #command = "fuse-sdl "+name+" --speed 100 --full-screen --graphics-filter hq3x  -j  --rom-"+model+" "+biosStr
        biosCommand= self.getBiosCommand(model, bios)
        command = ultraviolet.gameRunner.gameRunner.configuration.fuseCommand+" "+name+ biosCommand+" --fastload  --speed 100 --full-screen --graphics-filter hq3x  -j /dev/js0 --joystick-1-output 3 "
        print(command)
        os.system(command)
        return 1

    def getBiosCommand (self, model, bios):
        biosName= bios.replace(".zip","")
        biosName= bios.replace(".rom","")
        biosName= biosName.replace("-0","")
        biosName= biosName.replace("-1","")
        res=""
        if model =="48":
            res= " --machine "+model+" --rom-"+model+" "+bios
        elif model =="128":
            res = " --machine "+model+" --rom-"+model+"-0 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-1.rom "
        elif model=="plus2":
            res = " --machine "+model+" --rom-"+model+"-0 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-1.rom "
        elif model=="plus3":
            res = " --machine "+model+" --rom-"+model+"-0 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-1.rom  --rom-"+model+"-2 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-2.rom --rom-"+model+"-3 "+os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_BIOS_FOLDER+biosName+"-3.rom "
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
        files = listdir(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+ultraviolet.apputils.TMP_FOLDER+game.name)
        return files


