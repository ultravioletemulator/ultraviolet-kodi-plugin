import ultraviol.dataStructures

import shutil
import os
import zipfile

import ultraviol.MetadataProviderDbIndexWorldOfSpectrum

class PlatformProviderSpectrum:
    id = 1
    name = "Zx Spectrum"
    conf=None
    metadataProvider = ultraviol.MetadataProviderDbIndexWorldOfSpectrum.MetadataProviderDbIndexWorldOfSpectrum()


    def f(self):
        return 'hello world'


    def searchRom (self, queryString):

        # metadataProvider = MetadataProviderTgdb.MetadataProviderTgdb()
        #metadataProvider = ultraviolet.MetadataProviderWorldOfSpectrum.MetadataProviderWorldOfSpectrum()

        games = self.metadataProvider.searchGame(ultraviol.MetadataProviderDbIndexWorldOfSpectrum.MetadataProviderDbIndexWorldOfSpectrum.SPECTRUM_ID, queryString)
        resGameList = []
        resGameIdList = []
        i=0
        for game in games:
            gameId = game.id
            gameTitle = game.name
            print("(%s) %s" % (i, gameTitle))
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

        return selectedGame


    # def sRom (query):
#     print(" searching for rom: %s" % (query))
#     return ['1', '2', '3']

    def saveFile (self, source, dest):
        import os.path
        dirName = os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+"download"
        if (not os.path.exists(dirName)):
            os.mkdir(dirName)
            if (ultraviol.gameRunner.conf.download):
                shutil.copy(source, dirName+"/"+dest)

    def getRom(self, gameId):

        self.metadataProvider.downloadRom(gameId)


    def unzipFile (self, prefix, file):
        fh = open(file, 'rb')
        newName = file.replace(".zip","")
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            outpath = prefix
            z.extract(name, outpath)
        fh.close()


# http = urllib3.PoolManager()
        # r = http.request('GET', game.fileUrl)
        # with open(path, 'wb') as out:
        # while True:
        #     data = r.read(chunk_size)
        #     if data is None:
        #         break
        #     out.write(data)
        #
        # r.release_conn()
        return "Zip file"


    def listFile (self, name):
        return ['rom1','rom2']


    def playRom (self, model, bios, name):
        print("Playing rom: %s" % name)
        print("Model %s bios %s" % (model, bios))

        try:
            shutil.rmtree(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER)
        except:
            print("")

        if (bios.endswith(".zip")):
            nameClean=bios.replace(".zip", "")
            self.unzipFile(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER, ultraviol.gameRunner.gameRunner.BIOSFOLDER +model+"/"+bios)

        # os.system("fuse-sdl "+name+" --rom-128 bios/"+bios)
        bioses = os.listdir(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER)
        biosStr=""
        for bios in bioses:
            biosStr += os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+bios+" "

        # command = "fuse-sdl "+name+" --rom-speccyboot "+biosStr
        #command = "fuse-sdl "+name+" --speed 100 --full-screen --graphics-filter hq3x  -j  --rom-"+model+" "+biosStr
        biosCommand= self.getBiosCommand(model, bios)
        command = ultraviol.gameRunner.gameRunner.configuration.fuseCommand+" "+name+ biosCommand+" --fastload  --speed 100 --full-screen --graphics-filter hq3x  -j /dev/js0 --joystick-1-output 3 "
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
            res = " --machine "+model+" --rom-"+model+"-0 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-1.rom "
        elif model=="plus2":
            res = " --machine "+model+" --rom-"+model+"-0 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-1.rom "
        elif model=="plus3":
            res = " --machine "+model+" --rom-"+model+"-0 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-0.rom --rom-"+model+"-1 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-1.rom  --rom-"+model+"-2 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-2.rom --rom-"+model+"-3 "+os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER+biosName+"-3.rom "
        return res

    def downloadArt (self, name):
        return "art"


    def downloadCover (self, name):
        return "cover"


    def downloadSummary (self, game):
        print("Downloading summary for %s..." % (game.name))
        return "summary"

    def closeRom (self, game):
        print("Closing  %s" % game.name)
        shutil.rmtree("./"+game.name)

    def listZipRoms (self, game):
        from os import listdir
        files = listdir(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+"tmp/"+game.name)
        return files


