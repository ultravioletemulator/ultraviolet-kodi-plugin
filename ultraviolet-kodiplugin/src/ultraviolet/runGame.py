__author__ = 'developer'

#from platform import PlatformProviderSpectrum
#import uvplatform

name = "rescate atlantida"

import PlatformProviderSpectrum
import MetadataProviderTgdb
import os
import apputils
import shutil
# from pps import PlatformProviderSpectrum

#provider = platform.PlatformProviderSpectrum()
provider = PlatformProviderSpectrum.PlatformProviderSpectrum()
metadataProvider = MetadataProviderTgdb.MetadataProviderTgdb()

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

gameFile = provider.downloadRom(selectedGame)

romList = provider.listZipRoms(selectedGame)

print("****************************")
print("%s roms:" % selectedGame.name)
print("****************************")
i=0
for rom in romList:
    print("(%d) rom %s..." % (i, rom))
    i +=1

option = input("Please enter the option of the rom you want to play...")
print(option)
print("Selected rom: %s" % option)
rom = romList[int(option)]
print("Runnign rom: %s" % rom)
fullRomName = "./tmp/"+selectedGame.name+"/"+rom



print("Select Zx Spectrum configuration...")
print("Select model.")
models =os.listdir("./bios")
i=0
for model in models:
    print("(%d) model %s..." % (i, model))
    i +=1

modelOpt = input("Select model:")

selectedModel = models[int(modelOpt)]



print("Select available bios-es for the model %s " % selectedModel)

bioses =os.listdir("./bios/"+selectedModel)
i=0
for bios in bioses:
    print("(%d) bios %s..." % (i, bios))
    i +=1

biosOpt = input("Select bios:")

selectedBios = bioses[int(biosOpt)]


provider.playRom(apputils.cleanString(selectedModel) ,apputils.cleanString(selectedBios) ,apputils.cleanString(fullRomName))

# artFile = provider.downloadArt(selectedGame)
#
# coverFile = provider.downloadCover(selectedGame)
#
# summaryFile = provider.downloadSummary(selectedGame)


# provider.closeRom(selectedGame)

shutil.rmtree("tmp.file")




