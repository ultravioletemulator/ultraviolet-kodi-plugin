__author__ = 'developer'

import zipfile
import urllib3
import os
import shutil
import ultraviol



TMP_FOLDER="/tmp/"
TMP_BIOS_FOLDER="/tmpbios/"
TMP_FILE="tmp.file"

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
    dirName = os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+"download"
    if (not os.path.exists(dirName)):
        os.mkdir(dirName)
        if (ultraviol.gameRunner.conf.download):
            shutil.copy(source, dirName+"/"+dest)



def downloadFile ( fileUrl, saveName):
  print("Downloading file from url %s ..." % (fileUrl))

  c = urllib3.PoolManager()
  tmpFileName= os.getenv("HOME")+ultraviol.gameRunner.gameRunner.APP_HOME+TMP_FILE
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


