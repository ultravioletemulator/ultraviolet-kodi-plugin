__author__ = 'developer'


class ZipHelper:
    fileName= "none"

def extract  (self):
    return ""


def listFiles (self):
    return ["f1","f2"]

def extractFile (self, name):
    return "file"



def filterFileNames (self, zipFile, extensions):
    fileList = ZipHelper.listFiles(ZipHelper, zipFile);
    romList = filterFiles(fileList, extensions);
    return romList




def filterFiles (files, extensions):
    res =[]

    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                res.extend(file)
    return res
