__author__ = 'developer'

import zipfile
import urllib3
import os
import shutil
import ultraviol



def cleanString( str):
    if not str is None:
        return str.replace("'", "")

def cleanStringOs(str):
    if not str is None:
        return str.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)").replace("'", "")

def getInput(msg, length):
    res = input(msg)
    if (res==None or (res!=None  and res=="" )):
        if (length>0):
            res = 0
    return res




def unzipFile ( prefix, file):
   print ("Unzipping file %s to %s "%(prefix,file))
   fh = open(file, 'rb')
   newName = file.replace(".zip","")
   z = zipfile.ZipFile(fh)
   for name in z.namelist():
        outpath = prefix
        z.extract(name, outpath)
   fh.close()



def saveFile (source, dest):
    import os.path
    dirName = os.getenv("HOME")+ultraviol.configuration.APP_HOME+ultraviol.configuration.DOWNLOAD_FOLDER
    if (not os.path.exists(dirName)):
        os.makedirs(dirName)
        if (ultraviol.configuration.download):
            shutil.copy(source, dirName+"/"+dest)



def downloadFile ( fileUrl, saveName):
  print("Downloading file from url %s ..." % (fileUrl))

  c = urllib3.PoolManager()
  tmpFileName= ultraviol.configuration.TMP_FOLDER+ultraviol.configuration.APP_HOME+ultraviol.configuration.TMP_FILE
  try:
    shutil.rmtree(tmpFileName)
  except:
    print("Could not delete temp file "+tmpFileName)
    with c.request('GET', fileUrl, preload_content=False) as resp, open(tmpFileName, 'wb') as out_file:
      shutil.copyfileobj(resp, out_file)
    resp.release_conn()

  print("Done downloading.")
  print("Saving file...")
  name = saveName
  ultraviol.apputils.saveFile(tmpFileName, name)


def getHomeFolder(appName):
    return os.environ("HOME")+"/"+appName


def getConfFolder ():
    return os.environ["HOME"]+ultraviol.configuration.APP_CONFIG_HOME+"/"+ultraviol.configuration.CONF_FOLDER

def getDbFolder ():
    return os.environ["HOME"]+ultraviol.configuration.APP_CONFIG_HOME+"/"+ultraviol.configuration.DB_FOLDER
