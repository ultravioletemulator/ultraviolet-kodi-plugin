__author__ = 'developer'

import os
import shutil

import ultraviol.gameRunner
import ultraviol.apputils



DB_NAME="ultraviolet.db"
DB_FOLDER= "db/"
BIOSFOLDER="ultraviol/bios/"

DOWNLOAD_FOLDER ="download"
TORRENT_FOLDER ="torrent"

PKG_HOME="/ultraviol/"


APP_HOME="/ultraviolet/"
APP_CONFIG_HOME="/.ultraviolet/"

TMP_FOLDER="/tmp/"
TMP_BIOS_FOLDER="/tmpbios/"
TMP_FILE="tmp.file"

CONF_FOLDER="configuration/"
CONF_FILE="configuration.pickle"

def createFolderStructure():

        foldername= ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME
        if (not os.path.exists(foldername)):
            os.mkdir(foldername)

        foldername= ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_FOLDER
        if (not os.path.exists(foldername)):
            os.mkdir(foldername)

        foldername= ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_BIOS_FOLDER
        if (not os.path.exists(foldername)):
            os.makedirs(foldername)

        confFolder= ultraviol.apputils.getConfFolder()
        print ("Creating folder :"+confFolder)
        if (not os.path.exists(confFolder)):
            os.makedirs(confFolder)

        print ("Creating db structure")
        if (not os.path.exists(ultraviol.apputils.getDbFolder())):
            os.makedirs(ultraviol.apputils.getDbFolder())

        print ("copying...")
        dbFolder = ultraviol.apputils.getDbFolder()
        dbFile = dbFolder+ultraviol.configuration.DB_NAME
        origDbName ="."+ultraviol.configuration.PKG_HOME+ultraviol.configuration.DB_FOLDER+ultraviol.configuration.DB_NAME
        if (not os.path.exists(dbFile)):
            print (" %r " % (os.path.exists(origDbName)))
            print ("copying %s to %s ..." % (origDbName, dbFolder))
            shutil.copy(origDbName, dbFolder)






def deleteConfiguration():
    print ("Deleting configuration...")
    confFileName =ultraviol.apputils.getConfFolder()+ultraviol.configuration.CONF_FOLDER+ultraviol.configuration.CONF_FILE
    if (os.path.exists(confFileName )):
        os.remove(confFileName)

def configureEmulator ():

        print("Select Zx Spectrum configuration...")

        conf=None
        if (os.path.exists(ultraviol.apputils.getConfFolder()+ultraviol.configuration.CONF_FOLDER+ultraviol.configuration. CONF_FILE)):
            print ("if")

            print("loading pickle...")
            import pickle
            confFileName= ultraviol.apputils.getConfFolder()+ultraviol.configuration.CONF_FOLDER+ultraviol.configuration.CONF_FILE
            print (confFileName)
            with open(confFileName, 'rb') as f:
                conf = pickle.load(f)

        else:
            conf =ultraviol.dataStructures.configuration()
            fuseCommand = ultraviol.apputils.getInputKeyb("Configure your fuse program name:")

            # fuseCommand= "fuse-sdl"


            conf.fuseCommand= fuseCommand

            print("Select model.")
            # print (os.path("."))
            print(os.path.dirname(os.path.realpath(".")))
            models =os.listdir(ultraviol.configuration.BIOSFOLDER)
            i=0
            for model in models:
                print("(%d) model %s..." % (i, model))
                i +=1

            modelOpt = ultraviol.apputils.getInput("Select model:",i)

            selectedModel = models[int(modelOpt)]

            print("Select available bios-es for the model %s " % selectedModel)

            bioses =os.listdir(ultraviol.configuration.BIOSFOLDER+selectedModel)
            i=0
            for bios in bioses:
                print("(%d) bios %s..." % (i, bios))
                i +=1

            biosOpt = ultraviol.apputils.getInput("Select bios:" , i)

            selectedBios = bioses[int(biosOpt)]

            conf.model= selectedModel
            conf.bios= selectedBios

            downloadOptList=[]
            downloadOptList.append("True")
            downloadOptList.append("False")

            print("(0) True")
            print("(1) False")

            downloadOpt = ultraviol.apputils.getInput("Keeo downloaded games", 2)
            print("opt: %s" % downloadOpt)
            download = downloadOptList[int(downloadOpt)]
            conf.download= bool(download)


            print ("Configuring input...")
            pathInput="/dev/input/js*"
            import glob
            inputs = glob.glob(pathInput)
            i=0
            for input in inputs:
                print("(%d) %s " %(i, input))
                i +=1
            selectedInput= ultraviol.apputils.getInput("Select input:", i)
            conf.inputPath=selectedInput
            print("Writing pickle...")
            import pickle
            with open(ultraviol.apputils.getConfFolder()+ultraviol.configuration.CONF_FILE, 'bw+') as f:
                pickle.dump(conf, f)

        print("Model: %s bios: %s " % (conf.model, conf.bios))
        return conf


def loadConfiguration():
    print("loading configuration...")
    import pickle
    fileName = ultraviol.apputils.getConfFolder()+ultraviol.configuration.CONF_FILE
    with open(fileName, 'rb') as f:
        conf= pickle.load(f)
        return conf
