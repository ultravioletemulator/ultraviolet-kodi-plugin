import xbmcaddon
import xbmcgui
import PlatformProviderSpectrum
import MetadataProvider
import MetadataProviderTgdb
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1= "Hellow World"
line2=  " some text"
line3   = " Using python"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)

 mdProvider = MetadataProviderTgdb()

platformProvider = PlatformProviderSpectrum()

romProviders = platformProvider.getRomProviders ()
launcher = Launcher()

def searchRom (name):
    games= mdProvider.searchGame (mdProvider,name)
    persent game list


def getRom(id):
    rom = None
    return rom

def playRom (id, name):
    rom = None
    while rom == None:
        response =urllib2.urlopen(...)
        romZip= response.read()
        extensions = platformProvider.getSupprotedExtensions(platformProvider)

        fileList = ZipHelper.listFiles(ZipHelper,romZip);

        romList = ZipHelper.filterFileNames (fileList,extensions);
        romName = romList[0]
        romFile = ZipHelper.extract(romName)

        launcher.launchGame(launcher,platformProvider , romFile)
    return None