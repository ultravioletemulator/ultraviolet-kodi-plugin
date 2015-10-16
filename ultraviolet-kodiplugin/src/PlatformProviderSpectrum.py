import dataStructures
import urllib3
import shutil
import os
import zipfile

class PlatformProviderSpectrum:
    id = 1
    name = "Zx Spectrum"


# def __init__(self):
#     print("initiating platform provider"+self.name)


    def f(self):
        return 'hello world'


    def searchRom (self, query):
        print("%s searching for rom: %s" % (self.name,query))
        list = []
        game = dataStructures.Game()
        game.name = "rescate atlantida"
        game.fileUrl = "http://www.worldofspectrum.org/pub/sinclair/games/r/RescateAtlantida.tzx.zip"
        list.append(game)

        game2 = dataStructures.Game()
        game2.name= "Emilio butragueño"
        game2.fileUrl="http://www.worldofspectrum.org/pub/sinclair/games/e/EmilioButraguenoFutbol.tzx.zip"
        list.append(game2)
        return list


# def sRom (query):
#     print(" searching for rom: %s" % (query))
#     return ['1', '2', '3']


    def downloadRom (self, game):
        print("Downloading game %s..." % game.name)
        c = urllib3.PoolManager()
        tmpFileName= "./tmp.file"
        # shutil.rmtree(tmpFileName)
        with c.request('GET',game.fileUrl, preload_content=False) as resp, open(tmpFileName, 'wb') as out_file:
            shutil.copyfileobj(resp, out_file)

        resp.release_conn()
        print("Done downloading.")
        print ("Unzipping file %s " % tmpFileName)

        self.unzipFile ("./tmp/", tmpFileName)

        # fh = open(tmpFileName, 'rb')
        # z = zipfile.ZipFile(fh)
        # for name in z.namelist():
        #     outpath = "./tmp/"+game.name
        #     z.extract(name, outpath)
        # fh.close()

    def unzipFile (self, prefix, file):
        fh = open(file, 'rb')
        newName = file.replace(".zip","")
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            outpath = prefix+newName
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

        if (bios.endswith(".zip")):
            nameClean=bios.replace(".zip", "")
            print(nameClean)
            self.unzipFile("./tmpbios/", "bios/"+model+"/"+bios)

        # os.system("fuse-sdl "+name+" --rom-128 bios/"+bios)
        bioses = os.listdir("tmpbios/")
        biosStr=""
        for bios in bioses:
            biosStr += bios

        # os.system("fuse-sdl "+name+" --rom-speccyboot "+biosStr)
        command = "fuse-sdl -tap "+name+" --rom-48 bios/48/48.rom"
        print(command)
        os.system(command)
        return 1


    def downloadArt (self, name):
        return "art"


    def downloadCover (self, name):
        return "cover"


    def downloadSummary (self, name):
        print("%s downloading summary for %s" % (self.name, name))
        return "summary"

    def closeRom (self, game):
        print("Closing  %s" % game.name)
        shutil.rmtree("./"+game.name)

    def listZipRoms (self, game):
        from os import listdir
        files = listdir("./tmp/"+game.name)
        return files


