__author__ = 'developer'

import ultraviol.gameRunner
import ultraviol.apputils
import os
import shutil


DB_NAME="db/ultraviolet.db"
BIOSFOLDER="ultraviol/bios/"

def createFolderStructure():

        foldername= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME
        if (not os.path.exists(foldername)):
            os.mkdir(foldername)

        foldername= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_FOLDER
        if (not os.path.exists(foldername)):
            os.mkdir(foldername)

        foldername= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.apputils.TMP_BIOS_FOLDER
        if (not os.path.exists(foldername)):
            os.mkdir(foldername)


        confFolder= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER
        print ("Creating folder :"+confFolder)
        if (not os.path.exists(confFolder)):
            os.mkdir(confFolder)

        print ("Creating db structure")
        if (not os.path.exists(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.DB_FOLDER)):
            os.mkdir(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.DB_FOLDER)

        if (not os.path.exists(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.DB_FOLDER+ultraviol.configuration.DB_NAME)):
            shutil.copy("."+ultraviol.gameRunner.gameRunner.PKG_HOME+ultraviol.configuration.DB_NAME, os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.DB_FOLDER)


def deleteConfiguration():
    print ("Deleting configuration...")
    confFileName =os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE
    if (os._exists(confFileName )):
        os.remove(  )

def configureEmulator ():

        print("Select Zx Spectrum configuration...")

        conf=None
        if (os.path.exists(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE)):
            print ("if")
            # import json
            # from pprint import pprint
            # with open(os.getenv("HOME")+ultraviolet.gameRunner.gameRunner.APP_HOME+self.CONF_FOLDER+'configuration.json') as data_file:
            #     conf = json.load(data_file)
            # pprint(conf)

            print("loading pickle...")
            import pickle
            confFileName= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner.CONF_FILE
            print (confFileName)
            with open(confFileName, 'rb') as f:
                conf = pickle.load(f)


        else:
            conf =ultraviol.dataStructures.configuration()
            fuseCommand = input ("Configure your fuse program name:")
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

            # jsonConf= JSONEncoder.encode(conf)
            # import json
            # with open(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE, 'w+') as outfile:
            # json.dump(jsonConf, outfile)
            # json.dumps(conf, default=lambda o: o.__dict__,
            #               sort_keys=True, indent=4)
            # with open(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE, "w+") as outfile:
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
            with open(os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+ultraviol.gameRunner.gameRunner.CONF_FOLDER+ultraviol.gameRunner.gameRunner. CONF_FILE, 'bw+') as f:
                pickle.dump(conf, f)

        print("Model: %s bios: %s " % (conf.model, conf.bios))
        return conf
